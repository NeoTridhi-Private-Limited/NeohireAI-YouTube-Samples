# LLM+P: the model translates, a classical planner does the planning
import re
from collections import deque
from mini_llm import call_model

problem = call_model("to_pddl", "Take the medicine box from store to ward 3")
start, goal = re.findall(r"\(at box (\w+)\)", problem)
print("problem:", problem)

ROOMS = {"store": ["corridor"], "corridor": ["store", "lift"],
         "lift": ["corridor", "ward3"], "ward3": ["lift"]}
def plan(start, goal):               # breadth-first search: a tiny planner
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        if path[-1] == goal: return path
        queue.extend(path + [r] for r in ROOMS[path[-1]] if r not in path)

steps = plan(start, goal)
print("plan:   ", " -> ".join(steps))
print("robot:  ", call_model("from_plan", " ".join(steps)))
