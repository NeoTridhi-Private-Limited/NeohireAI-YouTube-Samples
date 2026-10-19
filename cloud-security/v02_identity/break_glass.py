# Check emergency (break-glass) admin accounts against simple rules.
ACCOUNTS = [
    {"name": "bg-admin-1", "mfa": "security key", "alert": True,
     "days_since_test": 40},
    {"name": "bg-admin-2", "mfa": "sms code", "alert": False,
     "days_since_test": 400},
]
RULES = [
    ("phishing-resistant M F A",
     lambda a: a["mfa"] in ("security key", "passkey")),
    ("alert on every sign-in", lambda a: a["alert"]),
    ("tested in the last 90 days", lambda a: a["days_since_test"] <= 90),
]
ready = 0
for a in ACCOUNTS:
    failed = [name for name, check in RULES if not check(a)]
    ready += not failed
    print(a["name"], "ok" if not failed else "needs fixing")
    for name in failed:
        print("   missing:", name)
print(f"accounts: {len(ACCOUNTS)}, ready: {ready}, need at least 2 ready")
