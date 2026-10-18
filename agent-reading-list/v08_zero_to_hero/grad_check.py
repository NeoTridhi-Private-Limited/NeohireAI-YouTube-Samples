# Trust, but verify: compare backward() with a numerical derivative
from micrograd_lite import Value

def f(x):
    return (x * x * 0.5 - x).tanh()

h = 0.000001
for x0 in [0.8, -0.5, 1.5]:
    x = Value(x0)
    f(x).backward()
    numeric = (f(Value(x0 + h)).data - f(Value(x0 - h)).data) / (2 * h)
    print(f"x = {x0:4}  autograd {x.grad:.6f}  numeric {numeric:.6f}"
          f"  gap {abs(x.grad - numeric):.1e}")
