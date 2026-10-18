# Orchestrator-workers: the plan depends on the request itself
from mini_llm import call_model

def orchestrate(request):
    plan = call_model("plan", request).splitlines()      # decided now, not fixed
    print("Plan:", plan)
    results = [call_model("work", step) for step in plan]   # workers
    return f"{len(results)} change(s) ready: " + ", ".join(r[6:] for r in results)

print(orchestrate("Add GST to invoices: touch billing/tax.py and ui/invoice.py"))
print(orchestrate("Rename the login button in ui/login.py"))
