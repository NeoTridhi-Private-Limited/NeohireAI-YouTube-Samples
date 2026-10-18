# Chain of thought: ask for the steps, not just the answer
from mini_llm import call_model

q = "3 kurtas at 499 each, a 200 rupee coupon, then 40 rupees delivery"

print("direct answer:", call_model("solve", q))

print("step by step:")
for step in call_model("solve", q, think=True).split("\n"):
    print("  ", step)
