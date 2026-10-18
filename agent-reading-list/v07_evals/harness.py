# Runs every synthetic case through the assistant and the checks, keeping a trace of each one
from mini_llm import call_model, reset
from cases import make_cases
from checks import CHECKS


def run_all(version=1):
    reset()
    traces = []
    for i, (feature, text) in enumerate(make_cases(), 1):
        reply = call_model("reply", text, version=version)
        failed = [c.__name__ for c in CHECKS[feature] if not c(reply)]
        traces.append({"id": i, "feature": feature, "input": text, "output": reply,
                       "synthetic": True, "failed": failed})
    return traces


def pass_rates(traces):
    rates = {}
    for feature in CHECKS:
        group = [t for t in traces if t["feature"] == feature]
        rates[feature] = sum(not t["failed"] for t in group) / len(group)
    return rates
