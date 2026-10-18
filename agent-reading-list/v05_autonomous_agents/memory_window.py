# Short-term memory is the context window: old turns fall out
LIMIT = 25                                    # words the model can see
chat = ["My name is Kavya", "I ordered a phone, order A17",
        "It arrived with a cracked screen", "Can I get a replacement",
        "Also what is your return window",
        "And what was my order number again"]

def context(turns):
    kept, used = [], 0
    for t in reversed(turns):                 # newest first
        n = len(t.split())
        if used + n > LIMIT: break
        kept.insert(0, t); used += n
    return kept, used

kept, used = context(chat)
print(f"{len(chat)} turns, the model sees {len(kept)} ({used} words)")
print("oldest it sees:", kept[0])
print("can it see A17?", any("A17" in t for t in kept))
