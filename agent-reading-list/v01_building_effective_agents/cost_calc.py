# What each design costs for 1,000 support tickets (illustrative prices)
SMALL, LARGE = 0.2, 3.0                     # paise per call
designs = {
    "one large call":             1 * LARGE,
    "routing (90% small)":        0.9 * SMALL + 0.1 * LARGE + SMALL,
    "chain of 3 small calls":     3 * SMALL,
    "guard + answer in parallel": SMALL + LARGE,
    "agent, about 4 large calls": 4 * LARGE,
}
for name, paise in designs.items():
    print(f"{name:28} {paise * 1000 / 100:7.2f} rupees")
