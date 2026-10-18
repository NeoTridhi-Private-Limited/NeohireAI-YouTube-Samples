# Output guardrail: check the JSON against a schema, retry when it fails
import json
from mini_llm import call_model

SCHEMA = {"order_id": str, "issue": str,
          "priority": {"low", "medium", "high"}}

def check(raw):
    try: data = json.loads(raw)
    except json.JSONDecodeError: return None, "not valid JSON"
    for field, rule in SCHEMA.items():
        if field not in data: return None, f"missing {field}"
        v = data[field]
        if not (v in rule if isinstance(rule, set) else isinstance(v, rule)):
            return None, f"bad {field}: {v!r}"
    return data, "ok"

for msg in ["I was charged twice for A17", "Order B22 is very late"]:
    for attempt in (1, 2, 3):
        data, why = check(call_model("extract", msg, attempt=attempt))
        print(f"{msg:28} try {attempt}: {why}")
        if data: break
