# Memory stream: recency + importance + relevance (Generative Agents)
NOW = 24                                          # the hour right now
stream = [(1, 2, "had idli for breakfast"),       # (hour, importance, text)
          (3, 8, "manager said the audit is on friday"),
          (20, 3, "the lift on floor 2 is slow"),
          (23, 1, "watered the office plants")]

def recency(hour): return 0.9 ** (NOW - hour)     # fades every hour
def relevance(text, query):
    q = set(query.split())
    return len(q & set(text.split())) / len(q) if q else 0
def score(m, query):
    hour, importance, text = m
    return recency(hour) + importance / 10 + relevance(text, query)

for query in ["", "audit friday", "slow lift"]:
    top = sorted(stream, key=lambda m: -score(m, query))[:2]
    best = ", ".join(f"{m[2]} {score(m, query):.2f}" for m in top)
    print(f"{query or 'no query':<13} -> {best}")
