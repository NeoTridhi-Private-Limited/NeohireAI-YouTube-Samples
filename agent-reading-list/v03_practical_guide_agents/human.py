# Hand over to a person: after too many failures, or before a high-risk action
from mini_llm import call_model

MAX_FAILS, REFUND_LIMIT = 2, 5000

def understand(messages):
    for tries, m in enumerate(messages, 1):
        intent = call_model("intent", m)
        if intent != "unknown":
            return f"understood '{intent}' on try {tries}"
        if tries >= MAX_FAILS:
            return f"PERSON: still unclear after {tries} tries, transferring"
    return "waiting for the customer"

def refund(order, amount):
    if amount > REFUND_LIMIT:
        return f"PERSON: refund of {amount} on {order} needs approval"
    return f"agent: refund of {amount} on {order} done"

print(understand(["umm", "my parcel A17"]))
print(understand(["hmm", "the thing from last week", "you know"]))
print(refund("C31", 1899))
print(refund("B22", 64999))
