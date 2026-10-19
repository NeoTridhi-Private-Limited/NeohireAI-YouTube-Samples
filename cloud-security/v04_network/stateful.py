# A customer's browser (port 51514) calls the web server on port 443.
# Does the server's reply get back out?
REQUEST = {"src_port": 51514, "dst_port": 443}

def security_group(req):
    # stateful: it remembers the allowed request, so the reply goes out
    return req["dst_port"] == 443

def nacl(req, outbound_ports):
    # stateless: the reply is a new packet and needs its own rule
    return req["dst_port"] == 443 and req["src_port"] in outbound_ports

CASES = [
    ("security group, inbound 443 only", security_group(REQUEST)),
    ("NACL, inbound 443 only", nacl(REQUEST, range(0))),
    ("NACL + outbound 1024-65535", nacl(REQUEST, range(1024, 65536))),
]
for name, ok in CASES:
    print(f"{name:<34} reply {'delivered' if ok else 'DROPPED'}")
