# Tool safeguards: rate each tool's risk, let the rating decide what happens
from agent_kit import TOOLS

def rate(tool):
    score = (not tool.read_only) + (not tool.reversible) + 2 * tool.money
    return "low" if score == 0 else "medium" if score <= 2 else "high"

POLICY = {"low": "run it",
          "medium": "run it, and log it",
          "high": "pause, run checks, and ask a person if needed"}

for t in TOOLS.values():
    r = rate(t)
    print(f"{t.name:16}{r:8}{POLICY[r]}")
