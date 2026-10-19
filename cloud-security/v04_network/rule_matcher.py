# NSG-style rules: lowest priority number first, first match wins,
# and anything that matches no rule falls to a default deny.
from ipaddress import ip_address, ip_network
RULES = [  # priority, name, source range, port, action
    (100, "allow-https", "0.0.0.0/0", 443, "Allow"),
    (200, "allow-sql-from-app", "10.0.1.0/24", 1433, "Allow"),
    (300, "deny-rdp-internet", "0.0.0.0/0", 3389, "Deny"),
]

def check(src, port):
    for prio, name, cidr, p, action in sorted(RULES):
        if p == port and ip_address(src) in ip_network(cidr):
            return f"{action} by {name} ({prio})"
    return "Deny by default rule (65500)"

TRAFFIC = [("203.0.113.9", 443), ("10.0.1.25", 1433),
           ("203.0.113.9", 1433), ("198.51.100.7", 3389)]
for src, port in TRAFFIC:
    print(f"{src:<13} port {port:<5} {check(src, port)}")
