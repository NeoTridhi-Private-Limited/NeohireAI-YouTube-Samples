# Shared responsibility: who looks after what, in each service model.
DUTIES = ["your data", "who can access it", "app settings", "app code",
          "operating system", "physical network", "buildings and power"]
# how many duties, counted from the bottom, the cloud provider takes
PROVIDER_TAKES = {"On-premises": 0, "IaaS": 2, "PaaS": 3, "SaaS": 4}

def owner(duty, model):
    from_bottom = len(DUTIES) - DUTIES.index(duty)
    return "provider" if from_bottom <= PROVIDER_TAKES[model] else "you"

for model, n in PROVIDER_TAKES.items():
    print(f"{model:12} you {len(DUTIES) - n}   provider {n}")
always = [d for d in DUTIES
          if all(owner(d, m) == "you" for m in PROVIDER_TAKES)]
print("Always yours:", ", ".join(always))
owners = {owner("app settings", m) for m in PROVIDER_TAKES}
print("Public MRI bucket is an app setting. Owner:", owners.pop())
