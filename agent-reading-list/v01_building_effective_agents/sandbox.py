# Test agents in a sandbox: a dry-run switch makes every action harmless
DRY_RUN = True
done = []

def issue_refund(order, amount):
    if DRY_RUN:
        return f"[dry run] would refund {amount} on {order}"
    done.append((order, amount))
    return f"refunded {amount} on {order}"

for order, amount in [("A17", 499), ("A18", 1299)]:
    print(issue_refund(order, amount))
print("real refunds made:", len(done))
