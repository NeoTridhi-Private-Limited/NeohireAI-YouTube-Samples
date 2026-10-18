# Peek, don't load: look at the start, the end, and search a big log
from mini_llm import count_tokens

log = [f"10:{i % 60:02d} order A{i} payment ok" for i in range(50_000)]
log[31_337] = "10:17 order A31337 payment FAILED: UPI timeout"

whole = count_tokens("\n".join(log))
head, tail = log[:3], log[-2:]                     # like head and tail
hits = [line for line in log if "FAILED" in line]  # like grep
peek = count_tokens("\n".join(head + tail + hits))
print(f"load the whole log : {whole:,} tokens")
print(f"head, tail, search : {peek} tokens")
print("found:", hits[0])
