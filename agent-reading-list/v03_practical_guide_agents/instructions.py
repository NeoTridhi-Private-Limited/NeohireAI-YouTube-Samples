# Instructions from an existing procedure: a help article becomes a routine
from mini_llm import call_model

HELP_ARTICLE = """Returns policy. First, ask for the order number. Then
check the order status and the purchase date. Returns are allowed only
within 30 days. If the item is damaged, start a refund. If the order
number is missing, ask for it again. Refunds over 5000 rupees need a
manager's approval."""

routine = call_model("write_routine", HELP_ARTICLE)
print("Routine for the returns agent")
for step in routine:
    print(" ", step)
