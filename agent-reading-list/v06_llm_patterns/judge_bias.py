# LLM-as-judge: ask twice with the order swapped, count only agreed wins
from mini_llm import call_model

def judge(x, y):
    first = call_model("judge", a=x, b=y)      # x shown first
    second = call_model("judge", a=y, b=x)     # same pair, swapped
    if (first, second) == ("A", "B"): return "x wins"
    if (first, second) == ("B", "A"): return "y wins"
    return "tie: the verdict followed the position"

short = "Refund in 5 to 7 working days."
pairs = [(short, "Refunds take 5 to 7 working days."),
         (short, "Thank you for your patience, dear customer, your request "
                 "is very important to us and we value you.")]
for x, y in pairs:
    print("one order only:", "x wins" if call_model("judge", a=x, b=y) == "A"
          else "y wins", "| both orders:", judge(x, y))
