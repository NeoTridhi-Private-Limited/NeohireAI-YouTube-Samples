# Routing: classify first, then send to the right handler and model
from mini_llm import call_model

HANDLERS = {"refund": "refund desk", "technical": "tech support", "general": "FAQ bot"}
COST = {"easy": 0.2, "hard": 3.0}             # paise per call: small vs large model

tickets = ["I want my money back for order A17",
           "The app shows an error when I pay",
           "Do you deliver to Vijayawada?",
           "The courier broke my TV and I want a refund or I will take legal action"]

for t in tickets:
    kind = call_model("classify", t)
    level = call_model("difficulty", t)
    print(f"{kind:9} -> {HANDLERS[kind]:12} model: {level} ({COST[level]} paise)")
