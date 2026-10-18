# Why Functions: the app keeps the keys, the rules and the user's consent
import json
from mini_llm import call_model

APP_LIMIT = 2000                          # a rule only the app enforces

def app_pay_upi(to, amount, user_says_yes):   # runs on the phone
    if amount > APP_LIMIT:
        return f"blocked, over the app's {APP_LIMIT} limit"
    if not user_says_yes:
        return "cancelled by the user"
    return "paid, after the user entered the UPI PIN"

for text, yes in [("Pay 349 rupees to Lakshmi Tiffins", True),
                  ("Pay 349 rupees to Lakshmi Tiffins", False),
                  ("Pay 5000 rupees to Ravi Electricals", True)]:
    a = json.loads(call_model("pay_proposal", text))["args"]
    print(f"{a['amount']} to {a['to']} ->",
          app_pay_upi(**a, user_says_yes=yes))
