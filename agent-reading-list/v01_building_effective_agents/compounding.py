# Why long agent runs need checks: small errors multiply
for per_step in (0.99, 0.95, 0.90):
    row = [f"{per_step ** n:5.0%}" for n in (1, 5, 10, 20)]
    print(f"{per_step:.0%} per step ->", "  ".join(row), "(1, 5, 10, 20 steps)")
