# Defensive UX: cite the source, ask when unsure, hand over when lost
from hybrid_retrieval import search
from mini_llm import DOCS

SURE, MAYBE = 0.4, 0.2              # confidence thresholds, tuned on evals

def reply(question):
    score, page = search(question)
    if score >= SURE:               # confident: answer, and show the source
        return f"{DOCS[page]} [source: {page}]"
    if score >= MAYBE:              # unsure: say so, let the user confirm
        return f"Did you mean {page}? [yes] [no]"
    return "Not sure. Pick a topic, or chat with a person."

if __name__ == "__main__":
    for q in ["when will it arrive", "money back please", "new address"]:
        print(f"{q} ({search(q)[0]})\n  -> {reply(q)}")
