# Long-term memory: store facts as vectors, find them by inner product
VOCAB = ["refund", "delivery", "upi", "days", "hours", "address", "bank"]
def embed(text):                              # a toy embedding: word counts
    words = text.lower().split()
    return [words.count(w) for w in VOCAB]
def dot(a, b): return sum(x * y for x, y in zip(a, b))

facts = ["Refund reaches the bank in 5 to 7 days",
         "Delivery takes 3 to 5 days",
         "Failed UPI money returns in 48 hours",
         "You can change the delivery address before dispatch"]
store = [(embed(f), f) for f in facts]        # the vector store

for q in ["when will my refund reach my bank",
          "can I change my delivery address"]:
    best = max(store, key=lambda item: dot(embed(q), item[0]))
    print(f"{q}\n   -> {best[1]}")
