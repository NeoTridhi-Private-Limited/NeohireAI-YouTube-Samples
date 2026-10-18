# Train, dev and test: a model must be judged on names it never saw
import math, random
from collections import Counter
from names_data import NAMES

random.seed(3)
names = NAMES[:]
random.shuffle(names)
train, dev, test = names[:24], names[24:28], names[28:]
ABC = ".abcdefghijklmnopqrstuvwxyz"
counts = Counter((a, b) for n in train for a, b in zip("." + n, n + "."))

def loss(group, extra=0.1):
    pairs = [(a, b) for n in group for a, b in zip("." + n, n + ".")]
    return -sum(math.log((counts[a, b] + extra) / sum(counts[a, c] + extra
                for c in ABC)) for a, b in pairs) / len(pairs)

print(f"sizes: train {len(train)}, dev {len(dev)}, test {len(test)}")
print(f"loss on train {loss(train):.3f}  (names it learned from)")
print(f"loss on dev   {loss(dev):.3f}  (names it never saw)")
