# Correlation: three quiet events by one account become one loud incident
events = [  # (minute, account, action, note)
    (100, "nurse.app", "ConsoleLogin", "new country"),
    (104, "nurse.app", "CreateAccessKey", ""),
    (111, "nurse.app", "StopLogging", "trail hospital-audit"),
    (300, "it.admin", "StopLogging", "approved change CHG-42"),
]
CHAIN, WINDOW = ["ConsoleLogin", "CreateAccessKey", "StopLogging"], 30

def incidents(evts):
    by_user = {}
    for minute, user, action, _ in evts:
        by_user.setdefault(user, []).append((minute, action))
    for user, seq in by_user.items():
        span = seq[-1][0] - seq[0][0]
        if [a for _, a in seq] == CHAIN and span <= WINDOW:
            yield user, span

for minute, user, action, note in events:
    print(f"t={minute:<4} {user:<10} {action:<16} {note}".rstrip())
for user, span in incidents(events):
    print(f"INCIDENT high: {user} did the whole chain in {span} minutes")
