"""mini_llm.py - a tiny stand-in for a language model, so every sample runs anywhere, offline, for free.

Each call names a task ("classify", "draft", ...) and the stand-in answers like a well-behaved model would.
To use a real model, replace the body of call_model() with an API call (see README.md); the samples do not change.
"""
import re

KB = {  # a small knowledge base for a store's support desk
    "refund": "Refunds go back to the original payment method within 5-7 working days.",
    "delivery": "Standard delivery takes 3-5 days; metro cities usually 2 days.",
    "upi": "UPI payments that fail are auto-reversed by the bank within 48 hours.",
}

def call_model(task, text="", **kw):
    """One model call. task says what is asked; text is the input. Returns a string."""
    t = text.lower()
    if task == "classify":
        if any(w in t for w in ("refund", "money back", "return")): return "refund"
        if any(w in t for w in ("error", "crash", "not working", "failed")): return "technical"
        return "general"
    if task == "difficulty":
        return "hard" if len(t.split()) > 18 or "legal" in t else "easy"
    if task == "outline":
        return "1. Why it matters\n2. How it works\n3. One example"
    if task == "draft":
        return f"Draft: {kw.get('topic', text)} explained in three short parts."
    if task == "guard":
        return "unsafe" if any(w in t for w in ("password", "otp", "card number")) else "safe"
    if task == "answer":
        hit = next((v for k, v in KB.items() if k in t), None)
        return hit or "Let me connect you with a person who can help."
    if task == "review":
        reviewer = kw.get("reviewer", 0)
        risky = "eval(" in t or ("select" in t and "+" in t)
        return "vulnerable" if risky and reviewer != 2 else ("vulnerable" if "eval(" in t else "ok")
    if task == "plan":
        files = re.findall(r"\b[\w/]+\.py\b", text)
        return "\n".join(f"update {f}" for f in files) or "update main.py"
    if task == "work":
        return f"done: {text}"
    if task == "headline":
        n = kw.get("attempt", 1)
        return ["Our amazing new super fast UPI refunds for every single customer in India",
                "UPI refunds now in 2 hours, for every customer",
                "UPI refunds in 2 hours"][min(n, 3) - 1]
    if task == "critique":
        problems = []
        if len(text) > 50: problems.append("too long (max 50 characters)")
        if "2 hours" not in text: problems.append("say the actual speed")
        return "; ".join(problems) or "approve"
    if task == "extract_skills":                   # read a resume, list the skills it mentions
        known = ["python", "sql", "react", "typescript", "docker", "kubernetes", "java", "aws"]
        return ", ".join(k for k in known if k in t)
    if task == "match":                            # compare skills with a job's must-haves
        need = [s.strip() for s in kw.get("need", "").split(",")]
        have = [s.strip() for s in text.split(",") if s.strip()]
        hit = [s for s in need if s in have]
        return f"{len(hit)}/{len(need)} must-haves: {', '.join(hit) or 'none'}"
    if task == "summary":
        return f"Shortlist summary: {text}."
    if task == "next_action":                      # the agent decides its next step from what it has seen so far
        found = re.search(r"\b([A-Z]\d+)\b", text)
        oid = found.group(1) if found else "A17"
        if "lookup_order" not in text: return f"lookup_order {oid}"
        if "damaged" in text and "issue_refund" not in text: return f"issue_refund {oid}"
        amt = re.search(r"refund of (\d+)", text)
        if "queued" in text: return f"finish Refund of {amt.group(1)} started for order {oid}."
        return f"finish Waiting for a manager to approve order {oid}."
    raise ValueError(f"unknown task {task}")
