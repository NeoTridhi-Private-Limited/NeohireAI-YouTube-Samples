# A bigram model: probabilities from counts, sample names, measure the loss
import math, random
from collections import Counter
from names_data import NAMES

random.seed(42)
ABC = ".abcdefghijklmnopqrstuvwxyz"
pairs = [(a, b) for n in NAMES for a, b in zip("." + n, n + ".")]
counts = Counter(pairs)
def prob(a, b):                     # a tiny extra count: smoothing
    return (counts[a, b] + 0.01) / sum(counts[a, c] + 0.01 for c in ABC)
def sample(ch=".", out=""):
    while True:
        ch = random.choices(ABC, [prob(ch, c) for c in ABC])[0]
        if ch == ".":
            return out
        out += ch

print("new names:", ", ".join(sample() for _ in range(8)))
nll = -sum(math.log(prob(a, b)) for a, b in pairs) / len(pairs)
print(f"average negative log likelihood: {nll:.3f}")
print(f"a model that guesses evenly gets: {math.log(27):.3f}")
