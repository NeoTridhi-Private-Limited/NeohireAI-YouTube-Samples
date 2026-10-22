"""Monthly loan EMI, used by a bank's mobile app (the sample app)."""


def emi(principal, yearly_rate_percent, months):
    r = yearly_rate_percent / 12 / 100
    if r == 0:
        return round(principal / months, 2)
    k = (1 + r) ** months
    return round(principal * r * k / (k - 1), 2)
