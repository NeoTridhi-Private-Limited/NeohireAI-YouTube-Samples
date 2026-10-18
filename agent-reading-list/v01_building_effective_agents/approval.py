# A human checkpoint: the agent may refund small amounts, a person approves big ones
LIMIT = 5000                                    # rupees

def issue_refund(order, amount, approved_by=None):
    if amount > LIMIT and approved_by is None:
        return f"PAUSED: refund of {amount} on {order} needs a manager's approval"
    who = f" (approved by {approved_by})" if approved_by else ""
    return f"refund of {amount} queued for {order}{who}"

print(issue_refund("A17", 499))
print(issue_refund("B22", 64999))
print(issue_refund("B22", 64999, approved_by="Meera, store manager"))
