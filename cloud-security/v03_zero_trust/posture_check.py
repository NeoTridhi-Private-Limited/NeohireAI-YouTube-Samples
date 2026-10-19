# Device posture: is this laptop healthy enough to reach the app?
RULES = {
    "disk encrypted": lambda d: d["encrypted"],
    "screen lock": lambda d: d["screenlock"],
    "OS patched": lambda d: d["build"] >= 26100,
    "EDR running": lambda d: d["edr"],
}
DEVICES = {
    "support-laptop-07": dict(encrypted=True, screenlock=True,
                              build=26100, edr=True),
    "home-desktop": dict(encrypted=True, screenlock=True,
                         build=19045, edr=False),
    "rainbow-gaming-pc": dict(encrypted=False, screenlock=False,
                              build=26100, edr=False),
}
for name, d in DEVICES.items():
    failed = [rule for rule, ok in RULES.items() if not ok(d)]
    score = f"{len(RULES) - len(failed)}/{len(RULES)}"
    verdict = "PASS" if not failed else "FAIL: " + ", ".join(failed)
    print(f"{name:<18} {score}  {verdict}")
