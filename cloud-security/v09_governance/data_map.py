# A personal data map: what we hold, why, and should we still hold it?
from datetime import date
TODAY = date(2026, 10, 17)
data_map = [  # (dataset, purpose, consent, child data, collected, keep days)
    ("admissions", "school admission", True, True, date(2026, 6, 1), 730),
    ("old-alumni-list", "", False, False, date(2025, 6, 1), 365),
    ("bus-gps-trail", "child safety on buses", True, True,
     date(2026, 9, 1), 30),
    ("parent-phones", "fee reminders", True, False, date(2025, 4, 1), 1095),
]
for name, purpose, consent, child, collected, keep in data_map:
    issues = []
    if not purpose or not consent:
        issues.append("no clear purpose or consent")
    if (TODAY - collected).days > keep:
        issues.append(f"kept {(TODAY - collected).days - keep} days too long")
    if child:
        issues.append("child data: check parental consent")
    print(f"{name:<16} {'; '.join(issues) or 'ok'}")
