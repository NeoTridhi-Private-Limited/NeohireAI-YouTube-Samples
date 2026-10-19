# A tiny policy evaluator: an explicit deny wins, then an allow,
# and anything not allowed is denied by default.
from fnmatch import fnmatch
POLICY = [  # what the bank's reporting intern may do
    {"effect": "Allow", "action": "reports:Read", "resource": "reports/*"},
    {"effect": "Deny", "action": "*", "resource": "reports/salaries/*"},
]

def evaluate(action, resource):
    allowed = False
    for s in POLICY:
        if fnmatch(action, s["action"]) and fnmatch(resource, s["resource"]):
            if s["effect"] == "Deny":
                return "DENY  (explicit deny)"
            allowed = True
    return "ALLOW" if allowed else "DENY  (nothing allows it)"

for action, resource in [("reports:Read", "reports/loans/oct.csv"),
                         ("reports:Delete", "reports/loans/oct.csv"),
                         ("reports:Read", "reports/salaries/oct.csv"),
                         ("customers:Read", "customers/kyc.csv")]:
    print(f"{action:15} {resource:25} {evaluate(action, resource)}")
