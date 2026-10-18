# Context rot, a toy simulation: one fact hidden in more and more text
import random
from mini_llm import recall_chance

rng = random.Random(42)                 # fixed seed: same numbers every run
for size in (1_000, 8_000, 32_000, 128_000):
    asked = 200
    found = sum(rng.random() < recall_chance(size) for _ in range(asked))
    print(f"{size:>7,} tokens of context -> fact used {found / asked:.0%}")
print("A slow slide, not a cliff. Toy numbers, the shape is the point.")
