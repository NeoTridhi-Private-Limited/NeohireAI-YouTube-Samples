# Fix the bugs, re-run the very same tests, and compare
from harness import run_all, pass_rates
old, new = run_all(version=1), run_all(version=2)
before, after = pass_rates(old), pass_rates(new)
print(f"{'feature':9} {'v1':>5} {'v2':>5}")
for f in before:
    print(f"{f:9} {before[f]:5.0%} {after[f]:5.0%}")

def overall(traces):
    return sum(not t["failed"] for t in traces) / len(traces)

print(f"{'overall':9} {overall(old):5.0%} {overall(new):5.0%}")
print(new[5]["output"].splitlines()[0], "|", new[24]["output"][:28])
