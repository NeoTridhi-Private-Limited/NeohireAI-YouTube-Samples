# A Function: the model only PROPOSES the call, as JSON.
# The app (client side) runs it, with its own data and keys.
import json
from mini_llm import call_model

RESTAURANTS = [("Sri Sagar", "dosa", True, 120),
               ("Udupi Corner", "dosa", True, 90),
               ("Grill House", "biryani", False, 280),
               ("Dosa Hut", "dosa", True, 240)]

def show_restaurants(dish, veg, max_price):          # lives in the app
    return [n for n, d, v, p in RESTAURANTS
            if d == dish and v == veg and p <= max_price]

reply = call_model("function_call", "veg dosa near me under 200")
call = json.loads(reply)
print("Model proposes:", call["name"], call["args"])
print("App runs it ->", show_restaurants(**call["args"]))
