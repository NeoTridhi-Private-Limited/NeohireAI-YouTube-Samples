# An agent: the model picks each step, tools report what really happened
from mini_llm import call_model

ORDERS = {"A17": {"amount": 499, "status": "delivered_damaged"}}
def lookup_order(oid): return f"{oid}: status={ORDERS[oid]['status']}"
def issue_refund(oid): return f"refund of {ORDERS[oid]['amount']} queued for {oid}"
TOOLS = {"lookup_order": lookup_order, "issue_refund": issue_refund}

history = "Customer: my parcel A17 arrived broken"
for step in range(1, 6):                       # a stopping condition
    action = call_model("next_action", history)
    if action.startswith("finish"):
        print("Agent:", action[7:]); break
    name, arg = action.split()
    result = TOOLS[name](arg)                  # ground truth from the tool
    print(f"step {step}: {action} -> {result}")
    history += f"\n{action} -> {result}"
