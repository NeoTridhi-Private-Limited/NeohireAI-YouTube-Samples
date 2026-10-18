# Why parallel calls feel faster: three checks, one after another vs together
import time
from concurrent.futures import ThreadPoolExecutor

def check(name):                      # pretend each model call takes 0.5 s
    time.sleep(0.5)
    return name

checks = ["safety", "tone", "facts"]
t = time.time(); [check(c) for c in checks]
print(f"one after another: {time.time() - t:.1f} s")
t = time.time()
with ThreadPoolExecutor() as pool: list(pool.map(check, checks))
print(f"all together:      {time.time() - t:.1f} s")
