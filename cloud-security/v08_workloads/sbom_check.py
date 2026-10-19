# Which of our apps contain a vulnerable library? Ask the SBOMs.
SBOMS = {
    "netbanking":  {"log4j-core": "2.14.1", "jackson-databind": "2.13.4"},
    "loan-portal": {"log4j-core": "2.17.1", "spring-core": "5.3.30"},
    "atm-switch":  {"commons-text": "1.9", "log4j-core": "2.15.0"},
    "upi-gateway": {"netty": "4.1.100"},
}
FIRST_SAFE = {"log4j-core": "2.17.1", "commons-text": "1.10.0"}  # advisories

def ver(v):
    return tuple(int(x) for x in v.split("."))

for app, parts in SBOMS.items():
    bad = [f"{lib} {v}" for lib, v in parts.items()
           if lib in FIRST_SAFE and ver(v) < ver(FIRST_SAFE[lib])]
    print(f"{app:<12} {'PATCH  ' + ', '.join(bad) if bad else 'ok'}")
