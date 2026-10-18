# The eval system is also a data engine: keep only the best traces
from harness import run_all
from mini_llm import call_model
traces = run_all(version=1) + run_all(version=2)
kept = []
for t in traces:
    verdict, _ = call_model("judge", t["output"], version=2)
    if not t["failed"] and verdict == "good":      # level 1 and level 2
        kept.append({"prompt": t["input"], "completion": t["output"]})
print(len(traces), "traces,", len(kept), "kept for fine-tuning")
print(kept[-1])
