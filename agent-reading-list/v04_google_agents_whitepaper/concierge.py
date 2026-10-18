# The whole agent: ReAct over a data store, an extension and a function
import re
from mini_llm import call_model
from store import DOCS, search
from travel_tools import search_trains, book_ticket_ui

def run(goal, confirm):
    pad = f"Question: {goal}"
    for step in range(1, 7):                        # a step limit
        out = call_model("concierge", pad)
        if "Final Answer:" in out:
            return out.split("Final Answer: ")[1]
        tool, arg = re.search(r"Action: (\w+)\[(.*)\]", out).groups()
        if tool == "policy":   obs = DOCS[search(arg)[0][1]]  # data store
        elif tool == "trains": obs = search_trains(arg)       # extension
        else:                  obs = book_ticket_ui(arg, confirm)  # function
        print(f"{step}. {tool}[{arg}] -> {obs}")
        pad += f"\n{out}\nObservation: {obs}"

goal = "Book a train from Hyderabad to Bengaluru for Friday's client visit"
print("Agent:", run(goal, confirm=True))
print("Agent:", run(goal, confirm=False))
