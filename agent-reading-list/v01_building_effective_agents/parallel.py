# Parallelization: sectioning (guard + answer together) and voting
from concurrent.futures import ThreadPoolExecutor
from mini_llm import call_model

msg = "My refund is late, here is my card number 4111..."
with ThreadPoolExecutor() as pool:            # sectioning: two jobs at once
    guard = pool.submit(call_model, "guard", msg)
    answer = pool.submit(call_model, "answer", msg)
    print("guard:", guard.result(), "| answer:", answer.result()[:40], "...")

code = "query = 'select * from users where id=' + user_id"
votes = [call_model("review", code, reviewer=r) for r in range(3)]
print("votes:", votes)
print("flag it" if votes.count("vulnerable") >= 2 else "looks fine")
