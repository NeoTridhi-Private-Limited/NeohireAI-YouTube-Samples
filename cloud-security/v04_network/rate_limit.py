# A WAF rate rule during a sale: too many login tries from one IP
# inside a sliding window, and that IP is blocked for a while.
from collections import defaultdict, deque
LIMIT, WINDOW = 5, 10          # toy numbers: 5 requests per 10 seconds

# second, source IP: a shopper tries 3 times, a bot tries every second
REQUESTS = [(t, "198.51.100.20") for t in (0, 4, 9)]
REQUESTS += [(t, "203.0.113.66") for t in range(20)]
REQUESTS.sort()

seen = defaultdict(deque)
tally = defaultdict(lambda: {"allowed": 0, "blocked": 0})
for t, ip in REQUESTS:
    q = seen[ip]
    while q and q[0] <= t - WINDOW:
        q.popleft()
    q.append(t)
    tally[ip]["allowed" if len(q) <= LIMIT else "blocked"] += 1
for ip, n in tally.items():
    print(f"{ip:<14} allowed {n['allowed']:>2}, blocked {n['blocked']:>2}")
