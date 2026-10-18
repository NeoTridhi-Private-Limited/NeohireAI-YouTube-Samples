# Why smoothing: one unseen letter pair makes the loss infinite
import math
from collections import Counter
from names_data import NAMES

ABC = ".abcdefghijklmnopqrstuvwxyz"
counts = Counter((a, b) for n in NAMES for a, b in zip("." + n, n + "."))

def name_loss(name, extra):
    total = 0.0
    for a, b in zip("." + name, name + "."):
        p = (counts[a, b] + extra) / sum(counts[a, c] + extra for c in ABC)
        if p == 0:
            return float("inf")
        total -= math.log(p)
    return total / (len(name) + 1)

for name in ["priya", "anjali", "xavier"]:
    print(f"{name:>7}: no smoothing {name_loss(name, 0):6.3f}"
          f"   smoothing {name_loss(name, 0.01):6.3f}")
