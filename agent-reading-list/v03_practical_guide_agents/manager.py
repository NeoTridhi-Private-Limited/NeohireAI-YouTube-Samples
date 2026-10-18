# Manager pattern: one agent keeps the customer and calls specialists as tools
from mini_llm import call_model
from agent_kit import AGENTS, run_agent

def as_tool(agent):                          # wrap a whole agent as a tool
    return lambda request: run_agent(agent, request)

manager_tools = {f"{n}_agent": as_tool(AGENTS[n])
                 for n in ("orders", "refunds", "sales")}

message = "Where is A17? Refund C31, it came damaged. Offers on school bags?"
answers = []
for part in call_model("split_request", message):     # the manager plans
    tool = call_model("intent", part) + "_agent"
    answers.append(manager_tools[tool](part))
    print(f"manager calls {tool:14}-> {answers[-1]}")
print("manager replies to the customer, in one message:")
for a in answers:
    print("  -", a)
