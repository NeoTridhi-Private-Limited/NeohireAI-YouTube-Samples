# MRKL: a router sends each question to the right expert module
import operator
from mini_llm import call_model

OPS = {"*": operator.mul, "+": operator.add, "-": operator.sub}
def calculator(expr):
    a, op, b = expr.split()
    return str(OPS[op](int(a), int(b)))
WEATHER = {"chennai": "33 C, humid", "shimla": "12 C, clear"}
EXPERTS = {"calculator": calculator, "weather": WEATHER.get,
           "llm": lambda text: call_model("write", text)}

for q in ["What is 1499 times 3?", "What is the weather in Shimla today?",
          "Write a thank you note for our delivery partner"]:
    expert, arg = call_model("route", q)       # the model picks + extracts
    print(f"{expert}({arg!r}) -> {EXPERTS[expert](arg)}")
