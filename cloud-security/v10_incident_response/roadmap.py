# A posture roadmap: what each organisation has, and its next three steps.
ROADMAP = [  # controls in the order we recommend, earliest first
    "MFA for all", "No long-lived keys", "Audit logs", "Locked backups",
    "Guardrails", "Posture score", "SIEM alerts", "Tested playbooks",
    "Policy as code", "24x7 SOC",
]
orgs = {
    "Small store": {"MFA for all", "Audit logs"},
    "Mid hospital": {"MFA for all", "No long-lived keys", "Audit logs",
                     "Locked backups", "Guardrails"},
    "Large bank": set(ROADMAP) - {"Policy as code"},
}
for org, done in orgs.items():
    todo = [c for c in ROADMAP if c not in done][:3]
    pct = 100 * len(done) // len(ROADMAP)
    print(f"{org:<12} {pct:>3}%  next: {', '.join(todo)}")
