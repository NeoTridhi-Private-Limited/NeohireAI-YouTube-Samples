# Semantic caching can serve the wrong answer; an item ID key cannot
import math, re
from collections import Counter
from mini_llm import call_model

def similarity(a, b):                 # word cosine, like a loose embedding
    x, y = (Counter(re.findall(r"\w+", s.lower())) for s in (a, b))
    norm = math.hypot(*x.values()) * math.hypot(*y.values())
    return sum(x[w] * y[w] for w in x) / norm

old_q = "Summarise reviews of the Nova X12 phone"
new_q = "Summarise reviews of the Nova X13 phone"
cached = call_model("summary", "Nova X12")
s = similarity(old_q, new_q)
print(f"similarity {s:.2f}, above 0.8, so a semantic cache serves:")
print("  ", cached)

by_id = {"X12": cached}               # key = the product ID itself
item = "X13"
answer = by_id.get(item) or call_model("summary", "Nova X13")
print("item ID key", item, "->", answer)
