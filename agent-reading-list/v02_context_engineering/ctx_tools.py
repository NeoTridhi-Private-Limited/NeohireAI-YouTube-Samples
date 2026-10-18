# The context manager used by support_agent.py: a budget, compaction, notes
from pathlib import Path
import tempfile
from mini_llm import count_tokens, call_model

KB = {"broken": "Damaged parcels get a full refund of 499 to UPI in 2-3 days.",
      "emi": "EMI is available on orders above 3000.",
      "delivery": "Metro cities get delivery in 2 days."}
NOTES = Path(tempfile.gettempdir()) / "support_agent_NOTES.md"

def search_kb(message, max_tokens):       # just in time, within a budget
    found = [v for k, v in KB.items() if k in message.lower()]
    while found and sum(map(count_tokens, found)) > max_tokens:
        found.pop()                         # drop the weakest match
    return found

class Context:
    def __init__(self, budget, rules):
        self.budget, self.rules, self.turns = budget, rules, []
    def add(self, who, text): self.turns.append(f"{who}: {text}")
    def text(self): return "\n".join([self.rules] + self.turns)
    def tokens(self): return count_tokens(self.text())
    def compact(self, keep=2):              # summarise all but the latest turns
        summary = call_model("summarise", "\n".join(self.turns[:-keep]))
        self.turns = [summary] + self.turns[-keep:]

def save_note(line):                        # agentic memory, outside the window
    with NOTES.open("a", encoding="utf-8") as f: f.write(line + "\n")
def load_notes():
    return NOTES.read_text(encoding="utf-8") if NOTES.exists() else ""
def clear_notes(): NOTES.unlink(missing_ok=True)
