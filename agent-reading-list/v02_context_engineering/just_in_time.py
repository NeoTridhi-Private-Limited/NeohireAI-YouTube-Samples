# Up front or just in time: keep references, load only what the task needs
from mini_llm import count_tokens, call_model

NAMES = ("refunds", "delivery", "returns", "warranty", "upi", "emi",
         "gift_cards", "loyalty", "privacy", "sellers")
DOCS = {f"policies/{n}.md": f"Policy text about {n}. " * 150 for n in NAMES}
def read_file(path):                            # a tool the agent can call
    return DOCS[path]

question = "My UPI refund has not arrived"
upfront = sum(count_tokens(text) for text in DOCS.values())
index = "\n".join(DOCS)                         # only the file names
chosen = call_model("choose_files", question, files=list(DOCS))
jit = count_tokens(index) + sum(count_tokens(read_file(p)) for p in chosen)
print(f"everything up front : {upfront:>6,} tokens")
print(f"index + files needed: {jit:>6,} tokens")
print("files read:", ", ".join(chosen))
