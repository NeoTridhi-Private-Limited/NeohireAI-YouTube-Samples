# The data flywheel: turn good, rated answers into fine-tuning examples
import json

FEEDBACK = [  # question, the answer shown, rating, the agent's correction
    ("Refund for A17?", "Refund in 5 to 7 working days.", "up", None),
    ("UPI failed, money gone", "Please wait.", "down",
     "The bank reverses a failed UPI payment within 48 hours."),
    ("COD limit?", "COD up to 10000 rupees.", "up", None),
    ("Is my data safe?", "Yes, totally guaranteed!", "down", None)]

examples = []
for q, shown, rating, fix in FEEDBACK:
    if rating == "up": examples.append({"prompt": q, "completion": shown})
    elif fix: examples.append({"prompt": q, "completion": fix})  # corrected
kept = len(examples)
print(f"kept {kept} of {len(FEEDBACK)}, dropped {len(FEEDBACK) - kept}")
for e in examples: print(json.dumps(e))
