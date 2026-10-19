# Defence in depth: each layer stops most attacks, none stops all.
# Illustrative rates for phishing emails sent to an online store's admins.
LAYERS = [("email filter", 0.90),
          ("staff who spot and report it", 0.50),
          ("M F A on the admin account", 0.90),
          ("alert on an odd admin sign-in", 0.60)]

attacks = 1000
print(f"phishing emails sent: {attacks}")
for name, stops in LAYERS:
    attacks = round(attacks * (1 - stops))
    print(f"after {name:30} {attacks} get through")
print("one layer alone at 90 percent would let", round(1000 * 0.1),
      "through")
