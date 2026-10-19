# A tiny DLP scanner: patterns plus a checksum, like the real services do
import re
def luhn(num):
    d = [int(c) for c in num if c.isdigit()][::-1]
    s = sum(x if i % 2 == 0 else (x * 2 - 9 if x > 4 else x * 2)
            for i, x in enumerate(d))
    return s % 10 == 0
RULES = {"PAN": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
         "AADHAAR": r"(?<!\d )\b\d{4} \d{4} \d{4}\b(?! \d)",
         "CARD": r"\b(?:\d{4} ){3}\d{4}\b"}
FILES = {"orders_export.csv": "Ravi, card 4111 1111 1111 1111, PAN ABCDE1234F",
         "test_orders.csv": "order 4111 1111 1111 1112, qty 2",
         "support_chat.txt": "my aadhaar is 2345 6789 0123, please update",
         "menu.txt": "masala dosa 80, filter coffee 30"}
for name, text in FILES.items():
    found = []
    for kind, pattern in RULES.items():
        for match in re.findall(pattern, text):
            if kind != "CARD" or luhn(match):   # a card must pass the checksum
                found.append(kind)
    verdict = "SENSITIVE: restrict, alert" if found else "clean"
    print(f"{name:18} {','.join(found) or '-':12} {verdict}")
