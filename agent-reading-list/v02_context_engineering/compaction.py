# Compaction: when the window is nearly full, summarise and start fresh
from mini_llm import count_tokens, call_model

LIMIT = 500
turns = [f"turn {i}: chat about delivery slots for A17" for i in range(1, 41)]
turns[4] = "turn 5: DECISION refund 499 to UPI, approved by Meera"
turns[11] = "turn 12: OPEN customer wants a GST invoice"
turns[20] = "turn 21: DECISION new delivery slot Saturday 10 am"

before = count_tokens("\n".join(turns))
if before > LIMIT * 0.8:                        # nearly full: compact
    summary = call_model("summarise", "\n".join(turns[:-3]))
    turns = [summary] + turns[-3:]              # keep the latest turns as is
after = count_tokens("\n".join(turns))
print(f"before: {before} tokens, after: {after}")
for item in turns[0].split(": ", 1)[1].split("; "):
    print("  kept:", item)
print("  plus the last 3 turns, word for word")
