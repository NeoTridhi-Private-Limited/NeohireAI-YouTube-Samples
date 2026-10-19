# A SOAR playbook: safe steps run automatically, risky ones wait for a person
alert = {"account": "nurse.app", "severity": "high", "ip": "203.0.113.7"}

STEPS = [  # (action, risky?)
    ("look up the IP address reputation", False),
    ("revoke all sessions of the account", False),
    ("disable the account's access keys", False),
    ("turn audit logging back on", False),
    ("page the on-call analyst", False),
    ("delete the account for good", True),
]

def run(alert, approved_by=None):
    for action, risky in STEPS:
        if risky and not approved_by:
            print(f"WAIT  {action}: a person must approve")
        else:
            print(f"DONE  {action} [{approved_by if risky else 'auto'}]")

if alert["severity"] == "high":
    print(f"Playbook for {alert['account']}, severity {alert['severity']}")
    run(alert)
