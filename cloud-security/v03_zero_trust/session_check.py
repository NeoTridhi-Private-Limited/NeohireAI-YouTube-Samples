# One check at sign-in is not enough: re-check as signals change.
EVENTS = [  # minute, what happened
    (0, "sign-in", "token valid for 60 minutes"),
    (15, "request", "open patient reports"),
    (20, "signal", "laptop reported stolen, device disabled"),
    (25, "request", "open patient reports"),
    (40, "request", "download MRI files"),
]

def run(continuous):
    revoked, results = False, []
    for minute, kind, what in EVENTS:
        if kind == "signal" and continuous:
            revoked = True
        if kind == "request":
            results.append(f"min {minute} {'BLOCKED' if revoked else 'ok'}")
    return ", ".join(results)

print("check at sign-in only:", run(continuous=False))
print("continuous checks:    ", run(continuous=True))
