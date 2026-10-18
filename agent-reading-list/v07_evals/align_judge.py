# Align the judge with human critiques, then measure it properly
from harness import run_all
from mini_llm import call_model
from labels import LABELS
traces = {t["id"]: t for t in run_all(version=1)}
for version in (1, 2):
    tp = fp = fn = same = 0
    for tid, (human, why) in LABELS.items():
        out = traces[tid]["output"]
        verdict, _ = call_model("judge", out, version=version)
        same += verdict == human
        tp += verdict == human == "bad"
        fp += verdict == "bad" != human
        fn += human == "bad" != verdict
        if version == 2 and verdict != human:
            print(f"  still missed #{tid}: {why}")
    print(f"judge v{version}  agree {same / len(LABELS):.0%}  "
          f"precision {tp / (tp + fp):.0%}  recall {tp / (tp + fn):.0%}")
