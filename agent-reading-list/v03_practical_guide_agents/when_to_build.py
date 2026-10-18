# Rules engine or agent? A UPI payment fraud check
from mini_llm import call_model

def rules_engine(payment):              # a checklist with one preset limit
    return "flag" if payment["amount"] > 50000 else "pass"

payments = [
    {"amount": 75000, "note": "monthly rent to the usual landlord"},
    {"amount": 9500, "note": "new device, new payee, 2 am"},
    {"amount": 1200, "note": "groceries at the usual shop"},
]
print(f"{'amount':>7}  {'rules':6}model")
for p in payments:
    judged = call_model("fraud_review", p["note"])  # weighs the context
    print(f"{p['amount']:>7}  {rules_engine(p):6}{judged}")
