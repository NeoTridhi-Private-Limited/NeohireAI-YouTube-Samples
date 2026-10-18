# Chain-of-Thought: ask for the steps, not just the answer
from mini_llm import call_model

bill = ("Hospital bill: consultation 1500 rupees, tests 2500 rupees. "
        "Insurance pays 80 percent of tests only. What does the patient pay?")

print("Direct answer:", call_model("direct", bill))
print("Step by step:")
print(call_model("cot", bill + " Think step by step."))
print("Check in code:", 1500 + 2500 - 2500 * 80 // 100)
