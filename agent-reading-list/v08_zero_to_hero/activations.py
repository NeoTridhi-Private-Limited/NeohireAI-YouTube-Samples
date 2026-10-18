# Activations: big inputs saturate tanh and kill gradients; normalising helps
import math, random

random.seed(1)
raw = [random.gauss(0, 6) for _ in range(1000)]     # badly scaled layer

def report(label, xs):
    outs = [math.tanh(x) for x in xs]
    stuck = sum(abs(t) > 0.99 for t in outs) / len(outs)
    grad = sum(1 - t * t for t in outs) / len(outs)
    print(f"{label:<11} saturated {stuck:5.1%}   average gradient {grad:.2f}")

mean = sum(raw) / len(raw)
std = (sum((x - mean) ** 2 for x in raw) / len(raw)) ** 0.5
normed = [(x - mean) / std for x in raw]           # the batch norm idea
report("raw", raw)
report("normalised", normed)
