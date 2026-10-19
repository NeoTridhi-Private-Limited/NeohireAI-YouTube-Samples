# Zero Trust: being on the office network earns no trust.
def decide(r):
    if not r["mfa"]:
        return "DENY", "no M F A"
    if not r["device_ok"]:
        return "DENY", "unhealthy device, even on office Wi-Fi"
    if r["action"] == "export customers" and r["role"] != "admin":
        return "DENY", "role does not allow it"
    return "ALLOW", "identity, device and role checked"

# (who, mfa done, device healthy, role, action)
REQUESTS = [
    ("admin, office laptop", True, True, "admin", "edit prices"),
    ("stolen admin password", False, False, "admin", "edit prices"),
    ("staff, unpatched laptop", True, False, "support", "read orders"),
    ("support, healthy laptop", True, True, "support", "export customers"),
]
for who, mfa, ok, role, action in REQUESTS:
    req = dict(mfa=mfa, device_ok=ok, role=role, action=action)
    verdict, why = decide(req)
    print(f"{who:24} {verdict:5} {why}")
