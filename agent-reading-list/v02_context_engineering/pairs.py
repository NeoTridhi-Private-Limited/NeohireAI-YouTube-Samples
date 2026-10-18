# Why long context is costly: every token looks at every other token
SIZES = (1_000, 10_000, 100_000)

def pairs(n):                       # n tokens -> n x n relationships
    return n * n

for n in SIZES:
    print(f"{n:>7,} tokens -> {pairs(n):>14,} token pairs to attend to")
growth = pairs(SIZES[1]) // pairs(SIZES[0])
print(f"10x more tokens -> {growth}x more pairs")
