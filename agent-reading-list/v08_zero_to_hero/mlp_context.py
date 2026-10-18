# The MLP idea: look at the last three letters to guess the next one
from names_data import NAMES

CONTEXT = 3
def examples(name):
    window = "." * CONTEXT
    for ch in name + ".":
        yield window, ch
        window = window[1:] + ch

for window, nxt in examples("priya"):
    print(f"  {window!r} -> {nxt!r}")
total = sum(len(n) + 1 for n in NAMES)
print("training examples from all names:", total)
print("possible 3-letter windows:", 27 ** CONTEXT,
      "so each letter gets a small vector")
