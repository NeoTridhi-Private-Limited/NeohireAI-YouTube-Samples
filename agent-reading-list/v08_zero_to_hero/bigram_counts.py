# Count which letter follows which, with '.' marking a name's start and end
from collections import Counter
from names_data import NAMES

pairs = Counter()
for name in NAMES:
    chars = "." + name + "."
    for a, b in zip(chars, chars[1:]):
        pairs[a + b] += 1

print(len(NAMES), "names,", sum(pairs.values()), "letter pairs,",
      len(pairs), "different pairs")
for pair, n in pairs.most_common(6):
    print(f"  {pair!r} seen {n} times")
