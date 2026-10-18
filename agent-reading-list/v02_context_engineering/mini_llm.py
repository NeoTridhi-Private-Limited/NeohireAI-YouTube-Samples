"""mini_llm.py - a tiny stand-in for a language model, so every sample runs anywhere, offline, for free.

It also counts tokens with a rough rule (about 4 characters per token) and has a toy "context rot"
curve. Both are simplifications for teaching, not measurements of any real model.
To use a real model, replace the body of call_model() with an API call (see README.md).
"""
import math
import re

STOP = {"a", "an", "the", "of", "by", "and", "for", "one", "is", "now", "my", "to", "what"}

def count_tokens(text):
    """Rough token count: about four characters per token."""
    return max(1, round(len(text) / 4))

def recall_chance(context_tokens):
    """Toy context rot: the chance of using a fact slides slowly as the context grows."""
    return max(0.3, 0.99 - 0.06 * math.log2(max(context_tokens, 1000) / 1000))

def _words(text):
    return {w for w in re.findall(r"[a-z0-9]+", text.lower().replace("'s", "")) if w not in STOP}

def _stems(text):
    return {w.rstrip("s") for w in _words(text)} - {"order", "please", "your", "you", "do"}

def call_model(task, text="", **kw):
    """One model call. task says what is asked; text is the input. Returns a string."""
    t = text.lower()
    if task == "pick_tool":                       # choose a tool by reading the descriptions
        scores = {n: len(_words(text) & _words(d)) for n, d in kw["tools"].items()}
        best = max(scores.values())
        top = [n for n, s in scores.items() if s == best]
        return top[0] if len(top) == 1 else "unsure: " + ", ".join(top)
    if task == "choose_files":                    # pick files by name, before reading them
        return [p for p in kw["files"] if p.split("/")[-1][:-3].rstrip("s") in t]
    if task == "summarise":                       # compaction: keep decisions, open items
        keep = []                                 # and what the agent already told
        for ln in text.splitlines():
            if "DECISION" in ln or "OPEN" in ln:
                keep.append(ln.split(": ", 1)[1])
            elif ln.startswith("agent: "):
                keep.append("told " + ln[7:].rstrip("."))
        return "Summary so far: " + "; ".join(keep)
    if task == "summarise_research":
        return {"why UPI refunds fail": "mostly bank timeouts, then wrong UPI IDs",
                "which couriers damage most parcels": "one courier, 3x the others",
                "top reasons for returns": "wrong size, then late delivery"}[text]
    if task == "answer":                          # answer only from what is in the context
        ctx = kw.get("context", "").lower()
        if "otp" in t and "never ask for otps" in ctx:
            return "For your safety, we never ask for an OTP."
        if "decide" in t:
            found = re.search(r"(A17: [^;\n]+)", kw.get("context", ""))
            return f"We agreed, {found.group(1)}." if found else "Sorry, I don't remember."
        best, reply = 0, "Let me check with a colleague."
        for line in kw.get("context", "").splitlines():
            if line.startswith(("customer:", "agent:")):
                continue                          # answer from facts, not from chat
            for sentence in re.split(r"(?<=\.) ", line.split(": ", 1)[-1]):
                score = len(_stems(text) & _stems(sentence))
                if score >= best and score and any(c.isdigit() for c in sentence):
                    best, reply = score, sentence.strip()
        return reply
    raise ValueError(f"unknown task {task}")
