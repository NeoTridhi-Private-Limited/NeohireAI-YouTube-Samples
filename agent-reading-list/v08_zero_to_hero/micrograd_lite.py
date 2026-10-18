# A tiny scalar autograd engine, written for this video in our own way.
# Each Value remembers its parents and how to pass its gradient back to them.
import math

class Value:
    def __init__(self, data, parents=()):
        self.data, self.grad, self.parents = data, 0.0, parents
        self._back = lambda: None

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other))
        def back():
            self.grad += out.grad
            other.grad += out.grad
        out._back = back
        return out
    __radd__ = __add__

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other))
        def back():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._back = back
        return out
    __rmul__ = __mul__

    def __sub__(self, other):
        return self + other * -1

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,))
        def back():
            self.grad += (1 - t * t) * out.grad
        out._back = back
        return out

    def backward(self):
        order, seen = [], set()
        def visit(v):                       # every node after its parents
            if v not in seen:
                seen.add(v)
                for p in v.parents:
                    visit(p)
                order.append(v)
        visit(self)
        self.grad = 1.0
        for v in reversed(order):           # walk back from the output
            v._back()
