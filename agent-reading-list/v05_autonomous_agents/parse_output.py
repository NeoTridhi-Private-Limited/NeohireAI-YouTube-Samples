# The fragile part: the agent's reply must be exact JSON
import json
from mini_llm import call_model

def ask(task, tries=3):
    for attempt in range(1, tries + 1):
        raw = call_model("agent_json", task, attempt=attempt)
        try:
            reply = json.loads(raw)
            if "command" in reply: return reply["command"]
            err = "missing the command field"
        except json.JSONDecodeError:
            err = "not valid JSON"
        print(f"attempt {attempt}: {err}")
        task += f"\nYour last reply was {err}. Reply in JSON only."

print("command:", ask("Check order A17"))
