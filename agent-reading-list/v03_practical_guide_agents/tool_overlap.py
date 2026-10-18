# Tool overload is about overlap, not only count: find tools that look alike
from itertools import combinations

TOOLS = {
    "get_order": "get the status of a customer order",
    "fetch_order": "fetch an order status for the customer",
    "track_parcel": "track where a parcel is with the courier",
    "issue_refund": "refund an order to the original payment",
    "search_kb": "search the store policy articles",
}
SMALL = {"the", "a", "an", "of", "for", "to", "is", "with", "where"}
def words(text): return set(text.split()) - SMALL

print(len(TOOLS), "tools checked")
for a, b in combinations(TOOLS, 2):
    wa, wb = words(TOOLS[a]), words(TOOLS[b])
    overlap = len(wa & wb) / len(wa | wb)
    if overlap >= 0.3:
        print(f"  {a} and {b}: {overlap:.0%} alike, merge or rename")
