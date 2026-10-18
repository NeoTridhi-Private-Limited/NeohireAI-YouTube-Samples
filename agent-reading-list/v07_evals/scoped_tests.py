# Scoped tests for one feature, the listing finder: three scenarios
from mini_llm import call_model, search
scenarios = [
    ("one match", "3 BHK in Hyderabad under 90 lakh", lambda n: n == 1),
    ("many matches", "3 BHK in Pune under 150 lakh", lambda n: n > 1),
    ("no match", "3 BHK in Chennai under 60 lakh", lambda n: n == 0)]

for name, text, ok in scenarios:
    query = call_model("query", text)          # the model writes the query
    n = len(search(query))                      # the CRM runs it
    verdict = "PASS" if ok(n) else "FAIL"
    print(f"{verdict} {name:12} {n} results  {list(query.values())}")
