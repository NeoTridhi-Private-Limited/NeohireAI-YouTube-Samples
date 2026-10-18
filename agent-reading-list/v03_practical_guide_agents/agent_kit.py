"""agent_kit.py - the small toolkit the samples share: typed tools, agents, and the run loop.

An online store's support desk. Orders, tools and agents are plain Python so you can read every line.
"""
from mini_llm import call_model

ORDERS = {  # order id: (item, amount in rupees, status)
    "A17": ("steel bottle", 499, "is out for delivery"),
    "C31": ("pressure cooker", 1899, "arrived damaged"),
    "B22": ("laptop", 64999, "arrived damaged"),
    "C99": ("study table", 3499, "is still packed"),
}
REFUND_LIMIT = 5000  # rupees; above this a person must approve


class Tool:
    """A standard tool definition: name, kind, description, and the facts that set its risk."""
    def __init__(self, name, kind, description, fn, read_only=True, reversible=True, money=False):
        self.name, self.kind, self.description, self.fn = name, kind, description, fn
        self.read_only, self.reversible, self.money = read_only, reversible, money

    def __call__(self, arg):
        return self.fn(arg)


class Agent:
    def __init__(self, name, instructions, tools=()):
        self.name, self.instructions = name, instructions
        self.tools = {t.name: t for t in tools}


def track_order(oid):
    if oid not in ORDERS: return f"No order {oid} found"
    item, _, status = ORDERS[oid]
    return f"{oid} ({item}) {status}"


def issue_refund(oid):
    item, amount, _ = ORDERS[oid]
    if amount > REFUND_LIMIT:                      # the limit lives in code, not in the prompt
        return f"Refund of {amount} for {oid} paused, a manager must approve it"
    return f"Refund of {amount} started for {oid}"


def search_catalog(query):
    if "school bag" in query.lower(): return "School bags, 3 on offer, from 699 rupees"
    return "Nothing on offer for that yet"


TOOLS = {t.name: t for t in [
    Tool("track_order", "data", "Find an order's status by ID, e.g. A17", track_order),
    Tool("search_kb", "data", "Look up a store policy, e.g. returns",
         lambda topic: call_model("answer", topic)),
    Tool("search_catalog", "data", "Find products and offers by name", search_catalog),
    Tool("send_sms", "action", "Text the customer a short update",
         lambda text: "SMS sent", read_only=False, reversible=False),
    Tool("issue_refund", "action", "Refund an order to the original payment",
         issue_refund, read_only=False, reversible=False, money=True),
]}

AGENTS = {
    "triage": Agent("triage", "First contact. Find out what the customer needs, then hand off."),
    "orders": Agent("orders", "Track orders and explain delivery.", [TOOLS["track_order"]]),
    "refunds": Agent("refunds", "Check the order, refund damaged items.",
                     [TOOLS["track_order"], TOOLS["issue_refund"]]),
    "sales": Agent("sales", "Help customers find products and offers.", [TOOLS["search_catalog"]]),
}


def run_agent(agent, message, max_turns=5):
    """The run loop: the model picks a step, a tool runs, the result goes back, until an exit."""
    history = [f"user: {message}"]
    for _ in range(max_turns):
        step = call_model("next_step", "\n".join(history), agent=agent.name)
        if step.startswith("final "):
            return step[6:]
        name, arg = step.split(maxsplit=1)
        if name not in agent.tools:
            return f"Error: {agent.name} has no tool {name}. Handing to a person."
        history.append(f"{name} -> {agent.tools[name](arg)}")
    return "Handing over to a person: too many turns."


# an agent can itself be a tool for another agent (orchestration)
TOOLS["refunds_agent"] = Tool("refunds_agent", "orchestration", "A specialist agent for refund cases",
                              lambda request: run_agent(AGENTS["refunds"], request),
                              read_only=False, reversible=False, money=True)
