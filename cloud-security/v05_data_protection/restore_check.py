# Ransomware at a school: which backups survive a stolen admin account?
VAULTS = {"plain vault":       {"locked": False, "soft_delete_days": 0},
          "soft-delete vault": {"locked": False, "soft_delete_days": 14},
          "locked vault":      {"locked": True,  "soft_delete_days": 14}}
ATTACK_DAY, NOTICED_DAY = 10, 26   # backups deleted on day 10, noticed on 26

def survives(v):
    if v["locked"]:
        return True, "delete refused: retention is locked"
    if NOTICED_DAY - ATTACK_DAY <= v["soft_delete_days"]:
        return True, "deleted, but still recoverable"
    return False, "deleted, recycle bin already emptied"

print(f"noticed {NOTICED_DAY - ATTACK_DAY} days after the attack")
for name, v in VAULTS.items():
    ok, why = survives(v)
    print(f"{name:18} {'RESTORE OK' if ok else 'LOST':10} {why}")
