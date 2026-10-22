"""Delivery fee for a small Bengaluru food app (the sample app)."""


def delivery_fee(distance_km, order_total):
    if order_total >= 499:
        return 0
    if distance_km <= 3:
        return 25
    return min(99, 25 + 8 * round(distance_km - 3))
