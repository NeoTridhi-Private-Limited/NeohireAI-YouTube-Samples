# One self-attention step: each word mixes in the words it finds relevant
import math

words = ["pay", "via", "upi"]
vecs = [[1.0, 0.0], [0.2, 0.9], [0.9, 0.4]]       # tiny made-up vectors

def softmax(xs):
    e = [math.exp(x - max(xs)) for x in xs]
    return [v / sum(e) for v in e]

def attend(causal):
    print("causal (no peeking ahead):" if causal else "full attention:")
    for i, q in enumerate(vecs):
        scores = [sum(a * b for a, b in zip(q, k)) / math.sqrt(2)
                  for k in vecs]
        if causal:
            scores = [s if j <= i else -1e9 for j, s in enumerate(scores)]
        w = softmax(scores)
        print(f"  {words[i]:>3} looks at", " ".join(f"{x:.2f}" for x in w))

attend(causal=False)
attend(causal=True)
