# Few-shot examples: a small, diverse set beats many similar ones
POOL = [("Where is my refund?", "refund"), ("Refund not received", "refund"),
        ("Money back please", "refund"),
        ("App crashes on login", "technical"),
        ("Payment page shows an error", "technical"),
        ("Do you deliver to Mysuru?", "delivery"),
        ("Parcel late by two days", "delivery"),
        ("Change my phone number", "account")]

first_three = POOL[:3]
diverse, seen = [], set()
for text, label in POOL:             # one canonical example per kind
    if label not in seen:
        diverse.append((text, label))
        seen.add(label)
print("first three cover:", sorted({label for _, label in first_three}))
print("diverse set covers:", sorted(seen))
for text, label in diverse:
    print(f"  {label:<10} {text}")
