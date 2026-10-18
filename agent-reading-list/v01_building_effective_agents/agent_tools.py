# Tools and the agent loop used by support_desk.py (same idea as agent.py)
from mini_llm import call_model

ORDERS = {"A17": {"amount": 499, "status": "delivered_damaged"}}
TOOLS = {
    "lookup_order": lambda oid: f"{oid}: status={ORDERS[oid]['status']}",
    "issue_refund": lambda oid: f"refund of {ORDERS[oid]['amount']} queued for {oid}",
}

def refund_agent(message, max_steps=5):
    history = f"Customer: {message}"
    for _ in range(max_steps):                             # stopping condition
        action = call_model("next_action", history)
        if action.startswith("finish"):
            return action[7:]
        name, arg = action.split()
        history += f"\n{action} -> {TOOLS[name](arg)}"     # ground truth
    return "Handing over to a person: too many steps."
