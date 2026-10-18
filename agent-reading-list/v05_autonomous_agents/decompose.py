# Task decomposition: three ways to break a big task into subgoals
from mini_llm import call_model

task = "Run the Diwali sale for our online store"

# 1. simple prompting: ask the model for the steps
print("model:   ", call_model("subgoals", task))

# 2. a task-specific instruction gives the plan its shape
print("template:", call_model("subgoals", task, style="a sale checklist"))

# 3. a person who knows the business writes the steps
human = ["ask the warehouse about stock", "get finance to approve discounts"]
print("human:   ", " -> ".join(human))
