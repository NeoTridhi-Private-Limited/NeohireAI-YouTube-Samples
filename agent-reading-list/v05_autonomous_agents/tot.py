# Tree of Thoughts: keep several partial plans alive, not just one
KM = {"DA": 2, "DB": 3, "DC": 9, "AB": 5, "AC": 1, "BC": 8}
def km(a, b): return KM.get(a + b) or KM[b + a]
def cost(path): return sum(km(a, b) for a, b in zip(path, path[1:]))

# one chain of thought: always ride to the nearest next stop
path = "D"
while len(path) < 4:
    left = [s for s in "ABC" if s not in path]
    path += min(left, key=lambda s: km(path[-1], s))
print("one chain:", "-".join(path), cost(path), "km")

# tree of thoughts: expand every option, keep the best 3 at each level
beam = ["D"]
for level in range(1, 4):
    options = [p + s for p in beam for s in "ABC" if s not in p]
    beam = sorted(options, key=cost)[:3]
    print(f"level {level}:", ", ".join(f"{p} {cost(p)}" for p in beam))
print("tree:", "-".join(beam[0]), cost(beam[0]), "km")
