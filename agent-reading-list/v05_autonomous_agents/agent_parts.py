# Memory and tools used by agent_main.py
STOP = {"the", "a", "is", "in", "to", "of", "for", "her", "with"}

class Memory:                                  # long-term memory
    def __init__(self): self.items = []
    def add(self, fact): self.items.append(fact)
    def recall(self, query):                   # best word overlap
        q = set(query.lower().split()) - STOP
        return max(self.items, key=lambda f: len(q & set(f.lower().split())))

def book_replacement(arg):
    if arg != "A17": return "error: use the order id"
    return "replacement R5 ships tomorrow"

TOOLS = {"lookup_order": lambda oid: f"{oid} delivered 4 days ago",
         "search_policy": lambda q: "replace within 7 days",
         "book_replacement": book_replacement,
         "reply": lambda lang: f"message sent in {lang}"}
