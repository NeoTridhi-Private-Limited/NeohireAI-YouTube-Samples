# Find risky long-lived access keys: leaked, old, or unused.
from datetime import date
TODAY = date(2026, 10, 17)
# (key owner, created, last used, seen in a public repo)
KEYS = [("ci-deploy", date(2026, 9, 30), date(2026, 10, 16), False),
        ("intern-reports", date(2026, 6, 2), date(2026, 10, 15), True),
        ("old-report-bot", date(2025, 1, 10), date(2025, 3, 1), False),
        ("ops-lead", date(2026, 3, 1), date(2026, 10, 10), False)]

for owner, created, last_used, leaked in KEYS:
    age, idle = (TODAY - created).days, (TODAY - last_used).days
    todo = []
    if leaked:
        todo.append("LEAKED: deactivate now")
    if age > 90:
        todo.append(f"{age} days old: rotate")
    if idle > 90:
        todo.append(f"unused {idle} days: delete")
    print(f"{owner:15} {', '.join(todo) or 'ok'}")
