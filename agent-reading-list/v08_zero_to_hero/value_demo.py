# A shop bill as a tiny graph: backward() finds how each input moves the bill
from micrograd_lite import Value

price, qty = Value(120.0), Value(3.0)
discount, tax = Value(-50.0), Value(1.18)
bill = (price * qty + discount) * tax
bill.backward()

print(f"bill = {bill.data:.2f}")
for name, v in [("price", price), ("qty", qty),
                ("discount", discount), ("tax", tax)]:
    print(f"{name:>8}: value {v.data:7.2f}   gradient {v.grad:7.2f}")
