# Create a contact, then look it up: the CRM should return exactly one
from mini_llm import call_model, lookup, reset
from cases import NAMES
reset()
passed = 0
for i, name in enumerate(NAMES):
    call_model("reply", f"Add {name}, phone 98480 {12345 + i}")
    found = len(lookup(name))
    passed += found == 1
    if found != 1:
        print(f"FAIL {name}: lookup returned {found} contacts")
print(f"{passed}/{len(NAMES)} passed")
