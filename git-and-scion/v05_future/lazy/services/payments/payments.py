def pay(order_id, amount):
    return {"order": order_id, "paid": amount}
def refund(order_id, amount):
    return {"order": order_id, "refunded": amount}
