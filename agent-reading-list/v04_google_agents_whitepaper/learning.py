# Targeted learning: fixed examples vs examples retrieved per request
from mini_llm import call_model
from store import vector, cosine
STORE = [("where is my parcel", "track_order"),
         ("I want my money back, the shoes are damaged", "refund"),
         ("my order has not arrived yet", "track_order"),
         ("change the delivery address to my parents house",
          "change_address"),
         ("cancel it, I ordered the wrong size by mistake", "cancel_order"),
         ("refund please, wrong item delivered", "refund")]
FIXED = STORE[:2]                            # in-context: always these two
def retrieved(request, k=2):                 # retrieval: the closest two
    q = vector(request)
    return sorted(STORE, key=lambda ex: -cosine(q, vector(ex[0])))[:k]
for req in ["The kurta is damaged, I want a refund",
            "Please send it to my office address instead",
            "I ordered by mistake, cancel please"]:
    a = call_model("pick_tool", req, examples=FIXED)
    b = call_model("pick_tool", req, examples=retrieved(req))
    print(req)
    print(f"   fixed examples: {a:12}  retrieved examples: {b}")
