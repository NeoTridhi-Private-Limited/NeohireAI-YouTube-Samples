# The whole help desk: cache, hybrid retrieval, model, guardrails, feedback
import re
from mini_llm import call_model, CALLS, DOCS
from hybrid_retrieval import search
from guard_pii import guard
from defensive_ux import SURE, MAYBE
cache, log = {}, []
def ask(q):
    key = " ".join(re.findall(r"[a-z0-9]+", q.lower()))  # normalised key
    if key in cache: return "cache", cache[key]
    score, page = search(q)                              # hybrid retrieval
    if score < MAYBE: return "handover", "Not sure. Chat with a person?"
    if score < SURE: return "confirm", f"Did you mean {page}?"
    status, cache[key] = guard(call_model("answer", q, context=DOCS[page]))
    return status.lower(), cache[key]                    # guarded, cached

for q in ["When will it arrive?", "when will it arrive", "Is COD available?",
          "Money back, call me on 9848012345", "Change my address"]:
    how, text = ask(q)
    log.append((guard(q)[1], how))                     # log it, without PII
    print(f"{how:8} {text}")
print("model calls:", CALLS["n"], "| logged:", log[3])
