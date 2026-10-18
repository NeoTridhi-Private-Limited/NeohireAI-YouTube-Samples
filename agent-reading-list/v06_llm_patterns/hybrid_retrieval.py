# Hybrid retrieval: exact keyword match + "embedding" similarity, blended
import math, re
from mini_llm import DOCS, embed

STOP = {"the", "my", "i", "a", "is", "will", "to", "in", "for", "want"}
def words(s): return [w for w in re.findall(r"[a-z0-9-]+", s.lower())
                      if w not in STOP]
def keyword(q, doc):          # share of query words found exactly (IDs)
    return sum(w in set(words(doc)) for w in words(q)) / len(words(q))
def semantic(q, doc):         # cosine of concept vectors (synonyms)
    a, b = embed(q), embed(doc)
    norm = math.hypot(*a.values()) * math.hypot(*b.values())
    return sum(a[k] * b[k] for k in a) / norm if norm else 0.0
def hybrid(q, doc): return 0.5 * keyword(q, doc) + 0.5 * semantic(q, doc)
def search(q, how=hybrid):    # best help page and its score
    return max((round(how(q, d), 2), k) for k, d in DOCS.items())

if __name__ == "__main__":
    for q in ["money back please", "checkout ERR-502", "when will it arrive"]:
        res = [search(q, f) for f in (keyword, semantic, hybrid)]
        print(f"{q:20}", " | ".join(f"{k if s else '-'} {s}" for s, k in res))
