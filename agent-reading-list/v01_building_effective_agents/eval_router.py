# Measure before you add complexity: how often does the router get it right?
from mini_llm import call_model

labelled = [
    ("Please refund order A17", "refund"),
    ("App crashed at payment", "technical"),
    ("Return my money now", "refund"),
    ("What are your store timings?", "general"),
    ("UPI failed but money debited", "technical"),
    ("Can I change my address?", "general"),
    ("I was charged twice for one order", "refund"),
]
right = 0
for text, expected in labelled:
    got = call_model("classify", text)
    right += got == expected
    print(f"{'ok ' if got == expected else 'MISS'} {text!r:36} -> {got}")
print(f"Accuracy: {right}/{len(labelled)}")
