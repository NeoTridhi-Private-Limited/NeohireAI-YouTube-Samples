# Caching: exact keys versus normalised keys, and the hit rate
import re
from mini_llm import call_model, CALLS

def normalise(q): return " ".join(re.findall(r"[a-z0-9]+", q.lower()))

questions = ["When will my refund come?", "when will my refund come",
             "When will my REFUND come?!", "Is COD available?",
             "is cod available", "When will my refund come?"]

for name, key in [("exact", lambda q: q), ("normalised", normalise)]:
    cache, hits, CALLS["n"] = {}, 0, 0
    for q in questions:
        k = key(q)
        if k in cache: hits += 1
        else: cache[k] = call_model("answer", q)       # a miss: ask the model
    print(f"{name:10} hits {hits}/{len(questions)}  model calls {CALLS['n']}"
          f"  hit rate {hits / len(questions):.0%}")
