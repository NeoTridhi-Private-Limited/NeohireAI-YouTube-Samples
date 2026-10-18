"""store.py - a tiny data store: documents turned into word-count vectors, searched by cosine similarity.
Real data stores use learned embeddings and a vector database; the idea is the same."""
import math
from collections import Counter
from mini_llm import words

DOCS = {
    "parental_leave": "Parental leave. A mother gets 26 weeks of paid leave after the baby is born, "
                      "a father 2 weeks.",
    "sick_leave": "Sick leave. 12 days of paid sick leave a year, a doctor's note after 3 days.",
    "work_from_home": "Work from home. You may work from home 2 days a week with your manager's approval.",
    "travel": "Travel policy. Trains up to 3A class, up to 2000 rupees a ticket.",
}

def vector(text):
    return Counter(words(text))

def cosine(a, b):
    dot = sum(a[w] * b[w] for w in a)
    size = math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values()))
    return dot / size if size else 0.0

INDEX = {name: vector(text) for name, text in DOCS.items()}   # built once, like loading a data store

def search(query, k=1):
    """Return the k best (score, document name) pairs, best first."""
    q = vector(query)
    return sorted(((round(cosine(q, v), 2), name) for name, v in INDEX.items()), reverse=True)[:k]
