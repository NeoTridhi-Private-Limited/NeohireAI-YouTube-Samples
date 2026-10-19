# A hospital ransomware incident: the timeline, and the numbers it gives us.
from datetime import datetime, timedelta
T = lambda hm: datetime(2026, 10, 3, *map(int, hm.split(":")))
events = [  # (time on 3 October, what happened)
    (T("01:40"), "first malicious login, phished VPN password"),
    (T("02:10"), "files start encrypting"),
    (T("02:25"), "alert raised by the SIEM"),
    (T("03:05"), "infected servers isolated"),
    (T("07:30"), "incident reported to CERT-In"),
    (T("19:00"), "records restored from the locked backup"),
]
(login, _), (encrypt, _), (alert, _), (isolate, _), (report, _), _ = events
for when, what in events:
    print(f"+{str(when - login):>8}  {what}")
on_time = report - alert <= timedelta(hours=6)
print(f"Detect {alert - encrypt}, contain {isolate - alert},",
      f"report {report - alert}", "(within 6 h)" if on_time else "(LATE)")
