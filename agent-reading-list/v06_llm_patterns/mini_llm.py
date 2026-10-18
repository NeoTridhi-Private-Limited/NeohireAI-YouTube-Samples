"""mini_llm.py - a tiny stand-in for a language model, so every sample runs anywhere, offline, for free.

Each call names a task ("answer", "judge", "extract", ...) and the stand-in answers the way a model might,
including some typical mistakes, so the patterns have something real to catch. To use a real model,
replace the body of call_model() with an API call (see README.md); the samples do not change.
"""
import json, re
from collections import Counter

DOCS = {  # a small help-desk knowledge base for an online store
    "refund": "Refunds reach the original payment method in 5 to 7 working days.",
    "upi": "A failed UPI payment is reversed by the bank within 48 hours.",
    "delivery": "Standard delivery takes 3 to 5 days, metro cities 2 days.",
    "cod": "Cash on delivery is available for orders up to 10000 rupees.",
    "err502": "Error ERR-502 means the payment gateway timed out, retry later.",
}

SYN = {  # stand-in "embedding": words that mean the same thing share a concept
    "refund": "refund", "refunds": "refund", "money": "refund", "back": "refund",
    "upi": "upi", "payment": "pay", "paid": "pay", "debited": "pay",
    "failed": "fail", "stuck": "fail", "reversed": "fail",
    "delivery": "ship", "deliver": "ship", "parcel": "ship", "courier": "ship",
    "days": "time", "when": "time", "long": "time", "arrive": "time",
    "cash": "cod", "cod": "cod", "gateway": "pay", "error": "fail",
}

def embed(text):
    """Bag of concepts: a crude stand-in for a real embedding model."""
    return Counter(SYN[w] for w in re.findall(r"[a-z0-9-]+", text.lower()) if w in SYN)

CALLS = {"n": 0}   # how many times the "model" was called (caching saves these)

def call_model(task, text="", **kw):
    """One model call. task says what is asked; text is the input. Returns a string."""
    CALLS["n"] += 1
    t = text.lower()
    if task == "answer":                      # prompt v1 is vague, v2 says: answer from the context
        if kw.get("prompt") == "v1":
            return "Thank you for writing to us, our team will get back to you soon."
        return kw.get("context") or "Sorry, I could not find that in our help pages."
    if task == "judge":                       # an LLM judge with typical biases
        a, b = kw["a"], kw["b"]
        return "B" if len(b) > 1.3 * len(a) else "A"   # likes long answers, and the first one
    if task == "extract":                     # complaint -> JSON; first try sometimes goes wrong
        if kw.get("attempt", 1) == 1 and "twice" in t:
            return '{"order_id": "A17", "issue": "charged twice"'          # cut off
        if kw.get("attempt", 1) == 1 and "late" in t:
            return '{"order_id": "B22", "issue": "late", "priority": "urgent!!"}'
        oid = (re.findall(r"\b[A-Z]\d+\b", text) or ["NA"])[0]
        issue = "charged twice" if "twice" in t else "late delivery" if "late" in t else "other"
        return json.dumps({"order_id": oid, "issue": issue, "priority": "high"})
    if task == "summary":                     # summarise reviews for one product
        return f"Summary of reviews for {text}: customers like it."
    raise ValueError(f"unknown task {task}")
