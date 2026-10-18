# The whole loop: evaluate, look at the failures, change, evaluate again
from collections import Counter
from harness import run_all, pass_rates
TARGET = 0.95                                 # a product decision

def evaluate(version):
    traces = run_all(version)
    overall = sum(not t["failed"] for t in traces) / len(traces)
    rates = {f: f"{r:.0%}" for f, r in pass_rates(traces).items()}
    print(f"v{version}: pass {overall:.0%} {rates}")
    top = Counter(c for t in traces for c in t["failed"]).most_common(1)
    return overall, top

for version in (1, 2):
    overall, top = evaluate(version)
    if overall >= TARGET:
        print(f"v{version} meets the {TARGET:.0%} target. Ship it.")
        break
    name, n = top[0]
    print(f"  below target. Biggest problem: {name}, {n} traces. Fix it.")
