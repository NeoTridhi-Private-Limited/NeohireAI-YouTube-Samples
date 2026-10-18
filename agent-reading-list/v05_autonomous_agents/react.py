# ReAct: Thought, Action, Observation, repeated until done
from mini_llm import call_model

TOOLS = {"search_policy": lambda q: "refunds allowed within 7 days",
         "order_age": lambda oid: "delivered 4 days ago"}

log = "Question: can order A17 still be refunded?"
for _ in range(4):                               # a step limit
    thought, action, arg = call_model("react", log)
    print("Thought:", thought)
    if action == "finish":
        print("Answer: ", arg); break
    obs = TOOLS[action](arg)                     # the real world answers
    print(f"Action:  {action}[{arg}]  Observation: {obs}")
    log += f"\n{thought}\n{action}[{arg}] -> {obs}"
