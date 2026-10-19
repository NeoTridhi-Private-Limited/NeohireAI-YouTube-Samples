# A posture score, like a secure score: weighted checks across resources
CHECKS = [  # (resource, check, weight, passing)
    ("bucket citizen-docs", "public access blocked",      10, False),
    ("vm web-01",           "SSH closed to internet",      8, False),
    ("db applications",     "encrypted with own key",     5, True),
    ("admin accounts",      "MFA for every admin",       10, True),
    ("vm web-01",           "OS patches under 30 days",   6, False),
    ("logging",             "audit logs kept 1 year",     4, True),
    ("storage backups",     "backup vault locked",        7, True),
]
total = sum(c[2] for c in CHECKS)
def score(checks):
    return round(100 * sum(c[2] for c in checks if c[3]) / total)
print(f"posture score: {score(CHECKS)}%")
failing = sorted((c for c in CHECKS if not c[3]), key=lambda c: -c[2])
for res, check, weight, _ in failing:
    print(f"  FIX  +{weight:<2} {res:20} {check}")
top = {(f[0], f[1]) for f in failing[:2]}
fixed = [(r, c, w, ok or (r, c) in top) for r, c, w, ok in CHECKS]
print(f"after fixing the top two: {score(fixed)}%")
