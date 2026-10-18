# Choosing what goes in: the most useful snippets that fit the budget
from mini_llm import count_tokens

SNIPPETS = [  # (relevance score from search, text)
    (0.92, "UPI order refunds go back to the same UPI ID in 2-3 days."),
    (0.88, "Damaged items are refunded once the courier picks them up."),
    (0.41, "Our store started in Pune in 2019 and ships to 900 cities."),
    (0.75, "Cash on delivery refunds go to a bank account you add."),
    (0.35, "Festive sale: extra 10% off on kitchen items this weekend."),
]
BUDGET, used, kept = 40, 0, 0
for score, text in sorted(SNIPPETS, reverse=True):
    n = count_tokens(text)
    if score < 0.5:
        print(f"drop {score:.2f}  too weak   {text[:30]}...")
    elif used + n > BUDGET:
        print(f"drop {score:.2f}  no room    {text[:30]}...")
    else:
        kept, used = kept + 1, used + n
        print(f"keep {score:.2f}  {n} tokens  {text[:30]}...")
print(f"context gets {kept} snippets, {used} of {BUDGET} tokens")
