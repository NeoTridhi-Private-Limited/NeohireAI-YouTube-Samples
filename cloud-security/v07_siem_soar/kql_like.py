# A tiny KQL-like filter: failed sign-ins, grouped, over a limit
from collections import Counter

logs = [("02:01", "admin@upi", "203.0.113.7", "fail")] * 14 + [
    ("02:09", "admin@upi", "203.0.113.7", "success"),
    ("09:15", "meera@upi", "198.51.100.4", "fail"),
    ("09:16", "meera@upi", "198.51.100.4", "success"),
]

def where(rows, test):
    return [r for r in rows if test(r)]

fails = where(logs, lambda r: r[3] == "fail")
counts = Counter((r[1], r[2]) for r in fails)  # count() by user, ip
for (user, ip), n in counts.items():
    if n > 10:                                   # where Failures > 10
        ok = where(logs, lambda r: r[1] == user and r[3] == "success")
        print(f"ALERT  {user} {ip}: {n} failures, then success {ok[0][0]}")
    else:
        print(f"ignore {user}: {n} failure, then success (a typo)")
