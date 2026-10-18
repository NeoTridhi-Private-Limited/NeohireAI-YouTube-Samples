# Nearest neighbour: brute force vs locality-sensitive hashing (LSH)
import random
rng = random.Random(42)
vecs = [[rng.uniform(-1, 1) for _ in range(8)] for _ in range(2000)]
query = [x + 0.03 for x in vecs[1234]]          # very close to item 1234
def dot(a, b): return sum(x * y for x, y in zip(a, b))
def dist(a, b): return sum((x - y) ** 2 for x, y in zip(a, b))

planes = [[rng.gauss(0, 1) for _ in range(8)] for _ in range(6)]
def bucket(v): return tuple(dot(p, v) > 0 for p in planes)   # 6 bits
table = {}
for i, v in enumerate(vecs):                    # index once, up front
    table.setdefault(bucket(v), []).append(i)

brute = min(range(len(vecs)), key=lambda i: dist(vecs[i], query))
cands = table[bucket(query)]                    # only one bucket
lsh = min(cands, key=lambda i: dist(vecs[i], query))
print(f"brute force: item {brute}, {len(vecs)} comparisons")
print(f"LSH:         item {lsh}, {len(cands)} comparisons")
print(f"buckets: {len(table)}, same answer: {brute == lsh}")
