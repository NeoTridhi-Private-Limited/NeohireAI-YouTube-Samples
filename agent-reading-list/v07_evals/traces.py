# Log every interaction as a trace: one JSON line each, here in memory
import io
import json
from harness import run_all
log = io.StringIO()
for t in run_all(version=1):
    log.write(json.dumps(t) + "\n")
lines = log.getvalue().splitlines()
print(len(lines), "traces logged")
t = json.loads(lines[31])
for key in ("id", "feature", "input", "output", "synthetic", "failed"):
    print(f"{key:9} {t[key]}")
