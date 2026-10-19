# An admission check, like Binary Authorization: may this image run?
TRUSTED = "registry.example.com/shop/"
images = [
    {"ref": TRUSTED + "web@sha256:9f1c", "signed": True, "critical": 0},
    {"ref": TRUSTED + "cart:latest", "signed": True, "critical": 0},
    {"ref": "docker.io/freebie/cache:1.0", "signed": False, "critical": 0},
    {"ref": TRUSTED + "pay@sha256:41ab", "signed": True, "critical": 2},
]

def decide(img):
    if not img["ref"].startswith(TRUSTED):
        return "DENY  untrusted registry"
    if not img["signed"]:
        return "DENY  not signed by our CI"
    if img["ref"].endswith(":latest"):
        return "DENY  use a digest, not latest"
    if img["critical"]:
        return f"DENY  {img['critical']} critical vulnerabilities"
    return "ALLOW"

for img in images:
    print(f"{decide(img):<34} {img['ref'].split('/')[-1]}")
