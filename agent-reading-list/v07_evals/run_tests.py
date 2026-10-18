# Run every check over all 48 synthetic inputs: a pass rate per feature
from collections import Counter
from harness import run_all, pass_rates
traces = run_all(version=1)
for feature, rate in pass_rates(traces).items():
    print(f"{feature:9} {rate:5.0%}")
failures = Counter(name for t in traces for name in t["failed"])
for name, n in failures.most_common():
    print(f"  {name:14} failed {n} times")
