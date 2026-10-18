# A model as judge, compared with a person's labels on the same 20 traces
from harness import run_all
from mini_llm import call_model
from labels import LABELS
traces = {t["id"]: t for t in run_all(version=1)}

def agreement(version):
    same = 0
    for tid, (human, _) in LABELS.items():
        out = traces[tid]["output"]
        verdict, _ = call_model("judge", out, version=version)
        same += verdict == human
    return same / len(LABELS)

bad = sum(h == "bad" for h, _ in LABELS.values())
print(f"human labels: {bad} bad, {len(LABELS) - bad} good")
print(f"judge v1 agrees with the human {agreement(1):.0%} of the time")
