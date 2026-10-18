# An agent = a model + tools + an orchestration layer (the loop)
from mini_llm import call_model

def track_order(oid):                                   # a tool
    return f"{oid}: out for delivery, 12 min away"
TOOLS = {"track_order": track_order}

history = "Customer: where is my order A42?"
for step in range(1, 5):                                # orchestration
    choice = call_model("decide", history)              # the model
    print(f"[model] {choice}")
    if choice.startswith("finish"):
        print(f"[loop]  goal reached in {step} steps"); break
    name, arg = choice.split()
    result = TOOLS[name](arg)
    print(f"[tool]  {result}")
    history += f"\n{choice} -> {result}"
