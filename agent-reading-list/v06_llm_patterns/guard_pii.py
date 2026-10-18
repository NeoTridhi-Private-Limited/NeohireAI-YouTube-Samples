# Output guardrails: redact personal data, block risky words, cap length
import re

PII = [("CARD", r"\b(?:\d{4} ?){3}\d{4}\b"),
       ("AADHAAR", r"\b\d{4} \d{4} \d{4}\b"),
       ("PHONE", r"\b[6-9]\d{9}\b"), ("EMAIL", r"\b[\w.]+@[\w.]+\.\w+\b")]
BLOCK, MAX_WORDS = {"guaranteed", "lawsuit"}, 25    # banned words, max length

def guard(text):
    for label, pattern in PII: text = re.sub(pattern, f"[{label}]", text)
    if any(w in text.lower() for w in BLOCK):
        return "BLOCKED", "Let me get a person."
    if len(text.split()) > MAX_WORDS:
        return "TRIMMED", " ".join(text.split()[:MAX_WORDS]) + " ..."
    return "OK", text

if __name__ == "__main__":
    for out in ["Call Ravi on 9848012345 or mail ravi@shop.in today.",
                "Card 4111 1111 1111 1111, Aadhaar 2345 6789 0123.",
                "Your refund is guaranteed by tomorrow.",
                "Refunds take 5 to 7 working days."]:
        print(*guard(out))
