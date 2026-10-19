# A CIS-style benchmark report: which checks pass, per section, and a score.
checks = [  # (section, check, passed)
    ("Identity", "MFA on every admin account", True),
    ("Identity", "No access keys on the root account", True),
    ("Identity", "Unused credentials removed after 45 days", False),
    ("Logging", "Audit log on in every region", True),
    ("Logging", "Log storage encrypted", True),
    ("Storage", "Public access blocked on all buckets", False),
    ("Network", "No SSH or RDP open to the whole internet", True),
    ("Keys", "Key rotation switched on", True),
]
sections = {}
for section, check, passed in checks:
    sections.setdefault(section, []).append(passed)
for section, results in sections.items():
    print(f"{section:<9} {sum(results)}/{len(results)} passed")
score = 100 * sum(p for _, _, p in checks) // len(checks)
print(f"Score: {score}%")
for _, check, passed in checks:
    if not passed:
        print("FIX:", check)
