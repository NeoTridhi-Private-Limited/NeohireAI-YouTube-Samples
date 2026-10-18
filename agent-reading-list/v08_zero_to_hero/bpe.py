# A toy byte pair encoder: merge the most common pair, again and again
from collections import Counter

text = "the payee paid the payment and the payer was paid"
ids = list(text.encode("utf-8"))
vocab = {i: bytes([i]) for i in range(256)}
print("start:", len(ids), "tokens (one per byte)")

for new_id in range(256, 260):
    top = Counter(zip(ids, ids[1:])).most_common(1)[0][0]
    vocab[new_id] = vocab[top[0]] + vocab[top[1]]
    out, i = [], 0
    while i < len(ids):
        if i + 1 < len(ids) and (ids[i], ids[i + 1]) == top:
            out.append(new_id); i += 2
        else:
            out.append(ids[i]); i += 1
    ids = out
    print(f"merge {vocab[new_id]!r} -> id {new_id}: {len(ids)} tokens")

print("decoded back:", b"".join(vocab[i] for i in ids).decode() == text)
