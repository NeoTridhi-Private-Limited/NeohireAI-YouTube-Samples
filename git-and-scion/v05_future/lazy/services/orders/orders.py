def place_order(item, qty):
    return {"item": item, "qty": qty, "status": "placed"}
def cancel_order(order_id):
    return {"order": order_id, "status": "cancelled"}
