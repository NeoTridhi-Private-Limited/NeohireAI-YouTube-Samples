# ReAct: Thought -> Action -> Observation, repeated until a final answer
import re
from mini_llm import call_model
from travel_tools import search_trains, check_seats

TOOLS = {"search_trains": search_trains, "check_seats": check_seats}
pad = "Question: a 3A train Hyderabad to Bengaluru tomorrow, under 1500"
for i in range(1, 6):                                   # a step limit
    out = call_model("react", pad)
    thought = out.split("\n")[0][9:]
    print(f"Thought {i}: {thought}")
    if "Final Answer:" in out:
        print("Final answer:", out.split("Final Answer: ")[1]); break
    tool, arg = re.search(r"Action: (\w+)\[(.*)\]", out).groups()
    obs = TOOLS[tool](arg)                              # the real result
    print(f"  Action {i}: {tool}[{arg}] -> {obs}")
    pad += f"\n{out}\nObservation: {obs}"
