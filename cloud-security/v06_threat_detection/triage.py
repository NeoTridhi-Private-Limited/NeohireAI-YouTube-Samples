# Diwali sale triage: which findings first? severity x exposure x data
SEV = {"critical": 4, "high": 3, "medium": 2, "low": 1}
FINDINGS = [  # (finding, severity, internet facing, touches customer data)
    ("old TLS on the offers site",     "medium",   True,  False),
    ("admin account without MFA",      "critical", True,  True),
    ("unpatched internal build VM",    "high",     False, False),
    ("order exports bucket is public", "high",     True,  True),
    ("access key unused for a year",   "medium",   False, True),
    ("debug logging left on",          "low",      False, False),
]
def risk(f):
    name, sev, internet, data = f
    return SEV[sev] * (3 if internet else 1) * (2 if data else 1)
ranked = sorted(FINDINGS, key=risk, reverse=True)
for f in ranked[:3]:
    print(f"FIX TODAY  risk {risk(f):>2}  {f[0]} ({f[1]})")
rest = ranked[3:]
print(f"this week: {len(rest)} more, risks {[risk(f) for f in rest]}")
