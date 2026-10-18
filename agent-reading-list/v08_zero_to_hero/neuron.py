# One neuron learns a rule: on time only if the trip is short AND roads clear
from micrograd_lite import Value

data = [((1, 1), 1), ((1, -1), -1), ((-1, 1), -1), ((-1, -1), -1)]
w1, w2, b = Value(0.1), Value(-0.2), Value(0.0)

for step in range(1, 41):
    loss = Value(0.0)
    for (x1, x2), y in data:
        err = (w1 * x1 + w2 * x2 + b).tanh() - y
        loss = loss + err * err
    for p in (w1, w2, b):
        p.grad = 0.0                      # forget the old gradients
    loss.backward()
    for p in (w1, w2, b):
        p.data -= 0.1 * p.grad            # a small step downhill
    if step in (1, 10, 40):
        print(f"step {step:2}: loss {loss.data:.3f}")

for (x1, x2), y in data:
    out = (w1 * x1 + w2 * x2 + b).tanh().data
    print(f"short={x1:2} light={x2:2} -> {out:5.2f}  (want {y:2})")
