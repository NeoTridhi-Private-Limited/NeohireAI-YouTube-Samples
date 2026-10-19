# Policy as code: check each new resource against guardrails, before deploy.
ALLOWED_REGIONS = {"centralindia", "asia-south1", "ap-south-1"}
RULES = [
    ("region outside India", lambda r: r["region"] in ALLOWED_REGIONS),
    ("public access", lambda r: not r["public"]),
    ("no owner tag", lambda r: bool(r["owner"])),
]
resources = [  # (name, region, public, owner tag)
    ("mri-reports", "us-east-1", True, ""),
    ("billing-db", "ap-south-1", False, "finance"),
    ("web-logs", "asia-south1", False, ""),
]
denied = 0
for name, region, public, owner in resources:
    r = {"region": region, "public": public, "owner": owner}
    broken = [rule for rule, ok in RULES if not ok(r)]
    denied += bool(broken)
    verdict = "DENY " if broken else "ALLOW"
    print(f"{verdict} {name:<12} {', '.join(broken) or 'all rules pass'}")
print(f"{denied} of {len(resources)} deployments blocked before they existed")
