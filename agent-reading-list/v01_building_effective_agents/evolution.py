# Grow the desk one step at a time, and measure each version on the same tickets
from mini_llm import call_model
from agent_tools import refund_agent

tickets = ["refund for broken parcel A17", "app error at payment", "delivery time to Pune?",
           "refund please, A17 arrived damaged", "UPI failed, money gone", "store timings?"]
def v1(t): return call_model("answer", t)                       # one call
def v2(t):                                                       # + routing
    k = call_model("classify", t)
    return "sent to tech support" if k == "technical" else call_model("answer", t)
def v3(t):                                                       # + agent for refunds
    return refund_agent(t) if call_model("classify", t) == "refund" else v2(t)

solved = lambda r: not r.startswith("Let me connect") and "Refunds go back" not in r
for name, fn in [("v1 one call", v1), ("v2 + routing", v2), ("v3 + agent", v3)]:
    print(f"{name:13} solved {sum(solved(fn(t)) for t in tickets)}/{len(tickets)}")
