# Level 3: an A/B test. Half the users get the new assistant (B).
import zlib
users = [f"agent{n:03d}" for n in range(400)]

def group(user):                  # stable: a user always sees the same one
    return "B" if zlib.crc32(user.encode()) % 2 else "A"

def booked_visit(user, g):        # simulated outcome, for this demo only
    rate = 22 if g == "A" else 29
    return zlib.crc32((user + g).encode()) % 100 < rate

for g in ("A", "B"):
    mine = [u for u in users if group(u) == g]
    booked = sum(booked_visit(u, g) for u in mine)
    print(f"group {g}: {len(mine)} users, {booked} booked a visit, "
          f"{booked / len(mine):.0%}")
