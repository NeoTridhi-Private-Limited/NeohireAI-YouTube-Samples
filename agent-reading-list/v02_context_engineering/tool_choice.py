# Overlapping tools confuse the model: if a person can't choose, nor can it
from mini_llm import call_model

BLOATED = {"get_order": "get an order's details",
           "fetch_order": "fetch details of an order",
           "order_info": "order details and history"}
CLEAN = {"lookup_order": "details of one order: status and amount, by ID",
         "track_parcel": "where a parcel is now, by tracking number",
         "issue_refund": "start a refund for one order, by order ID"}

request = "details of order A17"
for name, tools in (("bloated", BLOATED), ("clean", CLEAN)):
    choice = call_model("pick_tool", request, tools=tools)
    print(f"{name:<8} tool set -> {choice}")
