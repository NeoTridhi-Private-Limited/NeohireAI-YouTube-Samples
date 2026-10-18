# PII filter: check the model's reply before it reaches anyone
import re, textwrap

PATTERNS = {
    "card": r"\b(?:\d{4}[ -]?){3}\d{4}\b",
    "phone": r"\b[6-9]\d{9}\b",
    "email": r"\b[\w.]+@[\w.]+\.\w+\b",
}
def pii_filter(reply):
    found = []
    for kind, pattern in PATTERNS.items():
        reply, n = re.subn(pattern, f"[{kind} hidden]", reply)
        if n: found.append(kind)
    return reply, found

if __name__ == "__main__":
    draft = ("Hi Anil, we will call you on 9000012345. The refund to card "
             "4111 1111 1111 1111 is queued. A copy went to anil@example.com")
    clean, found = pii_filter(draft)
    print("found:", ", ".join(found))
    print(textwrap.fill(clean, 70))
