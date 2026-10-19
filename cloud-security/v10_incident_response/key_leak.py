# A leaked access key: what did the attacker do before we switched it off?
LEAKED_AT, KEY_OFF_AT = "09:00", "09:14"  # pushed to a public repo; disabled
OUR_IPS = {"10.20.0.5"}  # the bank's build server
audit_log = [  # (time, source IP, API call)
    ("08:55", "10.20.0.5", "PutObject statements/oct.pdf"),
    ("09:03", "203.0.113.9", "ListBuckets"),
    ("09:06", "203.0.113.9", "GetObject statements/oct.pdf"),
    ("09:11", "203.0.113.9", "RunInstances x20 (crypto mining)"),
    ("09:21", "203.0.113.9", "ListBuckets -> AccessDenied, key inactive"),
]
for time, ip, call in audit_log:
    if time < LEAKED_AT or ip in OUR_IPS:
        continue
    tag = "BLOCKED" if time >= KEY_OFF_AT else "ATTACKER"
    print(f"{time}  {tag:<8}  {ip:<12} {call}")
h1, m1 = map(int, LEAKED_AT.split(":"))
h2, m2 = map(int, KEY_OFF_AT.split(":"))
print(f"Window of exposure: {(h2 - h1) * 60 + m2 - m1} minutes")
