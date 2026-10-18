# Choosing models: a baseline with the large model, then try a small one
from mini_llm import call_model

EVALS = {
    "intent": [("where is my parcel", "orders"), ("refund me", "refunds"),
               ("app shows an error", "technical"), ("kurta price", "sales"),
               ("order not delivered", "orders"), ("bag offers", "sales")],
    "refund decision": [("parcel arrived damaged yesterday", "approve"),
                        ("wrong item delivered", "approve"),
                        ("damaged, bought 45 days ago", "deny"),
                        ("changed my mind, unopened, day 3", "approve")],
}
print(f"{'task':17}{'large':7}{'small':7}use")
for task, cases in EVALS.items():
    n = len(cases)
    score = {s: sum(call_model(task, q, size=s) == want for q, want in cases)
             for s in ("large", "small")}
    pick = "small model" if score["small"] == n else "large model"
    print(f"{task:17}{score['large']}/{n:<5}{score['small']}/{n:<5}{pick}")
