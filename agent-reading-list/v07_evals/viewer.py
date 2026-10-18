# A tiny trace viewer: filter to failures, one feature at a time
import json
from harness import run_all
log = "\n".join(json.dumps(t) for t in run_all(version=1))   # the JSONL log
traces = [json.loads(line) for line in log.splitlines()]

def view(feature=None, failed_only=True):
    for t in traces:
        if failed_only and not t["failed"]:
            continue
        if feature in (None, t["feature"]):
            yield t

for t in view(feature="listings"):
    first = t["output"].splitlines()[0]
    print(f"#{t['id']} {t['input']} -> {first} {t['failed']}")
print(sum(1 for _ in view()), "failures in all")
