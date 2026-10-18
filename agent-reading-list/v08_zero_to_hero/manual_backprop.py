# Backprop by hand: the chain rule, step by step, matches autograd
import math
from micrograd_lite import Value

x, w, b, target = 2.0, 0.3, -0.1, 1.0
# forward pass, one small step at a time
z = w * x + b
y = math.tanh(z)
loss = (y - target) ** 2
# backward pass by hand: multiply local slopes from the end
dy = 2 * (y - target)
dz = dy * (1 - y * y)
dw, db = dz * x, dz * 1.0
print(f"by hand : dw {dw:.5f}  db {db:.5f}")

W, B = Value(w), Value(b)
err = (W * x + B).tanh() - target
(err * err).backward()
print(f"autograd: dw {W.grad:.5f}  db {B.grad:.5f}")
