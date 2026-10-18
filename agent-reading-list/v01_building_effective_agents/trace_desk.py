# Transparency: log every step of one request through the support desk
from mini_llm import call_model
from agent_tools import TOOLS

log = []
def step(name, value):
    log.append(f"{len(log) + 1}. {name:10} -> {value}")
    return value

msg = "My parcel A17 arrived broken, I want a refund"
step("guard", call_model("guard", msg))
step("classify", call_model("classify", msg))
history = f"Customer: {msg}"
for _ in range(5):
    action = step("agent", call_model("next_action", history))
    if action.startswith("finish"): break
    name, arg = action.split()
    history += f"\n{action} -> " + step("tool", TOOLS[name](arg))
print("\n".join(log))
