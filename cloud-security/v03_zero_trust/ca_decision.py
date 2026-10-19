# Toy Conditional Access: every policy that matches adds a demand.
# A block beats everything; otherwise every demand must be met.
POLICIES = [
    (lambda s: s["risk"] == "high", "block"),
    (lambda s: s["app"] == "admin", "compliant device"),
    (lambda s: True, "mfa"),                      # all users, all apps
]

def decide(s):
    demands = {grant for when, grant in POLICIES if when(s)}
    if "block" in demands:
        return "BLOCK"
    missing = sorted(demands - s["proofs"])
    return "ALLOW" if not missing else "DENY, needs " + " + ".join(missing)

MFA, BOTH = {"mfa"}, {"mfa", "compliant device"}
SIGNINS = [("doctor, reports, ward PC", "low", "reports", MFA),
           ("IT admin, ward PC", "low", "admin", BOTH),
           ("IT admin, home PC", "low", "admin", MFA),
           ("phished admin, abroad", "high", "admin", MFA)]
for who, risk, app, proofs in SIGNINS:
    print(f"{who:<26} {decide(dict(risk=risk, app=app, proofs=proofs))}")
