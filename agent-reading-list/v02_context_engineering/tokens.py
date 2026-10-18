# A token budget: what fills the context window, and what is left
from mini_llm import count_tokens

BUDGET = 2000                       # a tiny window, so the numbers stay small
parts = {                           # repeated text stands in for longer text
    "system prompt": "You are the support assistant of a Pune store. " * 6,
    "tool definitions": "lookup_order(order_id): status and amount. " * 8,
    "chat history": "Customer asked about a late parcel and a refund. " * 20,
    "retrieved snippets": "Refunds reach the original payment method. " * 10,
}
used = 0
for name, text in parts.items():
    n = count_tokens(text)
    used += n
    print(f"{name:<20}{n:>5} tokens")
print(f"{'total used':<20}{used:>5} of {BUDGET}, {BUDGET - used} left")
