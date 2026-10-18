"""mini_llm.py - a tiny stand-in for a language model, so every sample runs anywhere, offline, for free.

Each call names a task ("intent", "next_step", ...) and the stand-in answers like a well-behaved model would.
To use a real model, replace the body of call_model() with an API call (see README.md); the samples do not change.
"""
import re

INTENTS = [  # checked in this order
    ("refunds", ("refund", "money back")),
    ("orders", ("where is", "parcel", "order", "deliver", "track")),
    ("technical", ("error", "crash", "otp not", "app ")),
    ("sales", ("price", "offer", "sell", "buy")),
]
ON_TOPIC = ("order", "refund", "return", "deliver", "parcel", "offer", "price", "payment",
            "upi", "kurta", "cooker", "laptop", "bag")
KB = {
    "return": "Returns are free within 30 days. Start one from My Orders.",
    "delivery": "Metro cities get delivery in 2 days, others in 3 to 5.",
}
ROUTINE = [  # (phrase in the help article, the clear step a good model would write)
    ("ask for the order number", "Ask: 'Please share your order number.'"),
    ("check the order status", "Call track_order with that number."),
    ("within 30 days", "If bought over 30 days ago, explain the policy, stop."),
    ("if the item is damaged", "If the status says damaged, call issue_refund."),
    ("order number is missing", "Edge case: no order number? Ask once more."),
    ("over 5000 rupees", "If the refund is over 5000 rupees, hand to a manager."),
]


def _intent(t):
    return next((kind for kind, words in INTENTS if any(w in t for w in words)), "unknown")


def _next_step(text, agent):
    """The agent's decision: call a tool, hand off, or give a final answer."""
    lines = text.splitlines()
    user = lines[0].lower()
    found = re.search(r"\b([A-Z]\d+)\b", lines[0])
    oid = found.group(1) if found else "A17"
    done = [l.split(" -> ")[0] for l in lines[1:]]
    last = lines[-1].split(" -> ", 1)[-1]
    if agent == "triage":
        return "handoff " + _intent(user)
    if "cancel" in user:
        return f"cancel_order {oid}"
    if agent == "sales":
        return f"search_catalog {lines[0][6:]}" if not done else f"final {last}"
    if "track_order" not in done or "until it moves" in user:
        return f"track_order {oid}"
    if agent == "refunds" and "damaged" in last and "issue_refund" not in done:
        return f"issue_refund {oid}"
    return f"final {last}"


def call_model(task, text="", **kw):
    """One model call. task says what is asked; text is the input. Returns a string (or a list)."""
    t = text.lower()
    if task == "intent":
        return _intent(t)
    if task == "fraud_review":                     # weigh the context, not one preset limit
        signals = [s for s in ("new device", "new payee", "2 am") if s in t]
        return "suspicious: " + ", ".join(signals) if len(signals) >= 2 else "looks normal"
    if task == "refund decision":
        days = re.search(r"(\d+) days ago", t)
        if kw.get("size") == "small":              # the small model misses the subtle cases
            return "approve" if ("damaged" in t or "wrong" in t) else "deny"
        if days and int(days.group(1)) > 30: return "deny"
        if "damaged" in t or "wrong item" in t: return "approve"
        return "approve" if "unopened" in t else "deny"
    if task == "write_routine":                    # turn a help article into numbered steps
        t = " ".join(t.split())
        steps = sorted((t.find(p), s) for p, s in ROUTINE if p in t)
        return [f"{i}. {s}" for i, (_, s) in enumerate(steps, 1)]
    if task == "next_step":
        return _next_step(text, kw.get("agent", "store"))
    if task == "split_request":                    # a manager breaks a message into parts
        return [p.strip() for p in re.split(r"[?.]", text) if p.strip()]
    if task == "safety":                           # jailbreaks and prompt injection
        bad = ("system prompt", "your instructions", "pretend you are", "role play")
        return "unsafe" if any(b in t for b in bad) else "safe"
    if task == "relevance":
        return "on-topic" if any(w in t for w in ON_TOPIC) else "off-topic"
    if task == "churn_risk":
        return "yes" if any(w in t for w in ("cancel my", "close my account", "leaving")) else "no"
    if task == "answer":
        hit = next((v for k, v in KB.items() if k in t), None)
        return hit or "Let me connect you with a person who can help."
    raise ValueError(f"unknown task {task}")
