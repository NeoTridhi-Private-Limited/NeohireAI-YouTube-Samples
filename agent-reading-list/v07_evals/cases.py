# Synthetic test inputs: many realistic requests from a few templates
from itertools import product
CITIES = ["Pune", "Hyderabad", "Bengaluru", "Chennai"]
NAMES = ["Ravi Kumar", "Anita Rao", "Imran Shaikh", "Lakshmi Iyer",
         "Arjun Mehta", "Fatima Khan", "Suresh Patil", "Divya Nair",
         "Karan Gill", "Meena Das", "Joseph Mathew", "Pooja Shah"]
def make_cases():
    cases = [("listings", f"{bhk} BHK in {city} under {budget} lakh")
             for city, bhk, budget in product(CITIES, (2, 3), (60, 90, 150))]
    for i, name in enumerate(NAMES):
        cases.append(("contacts", f"Add {name}, phone 98480 {12345 + i}"))
        day = ["Saturday", "Sunday", "Monday"][i % 3]
        when = "evening" if i % 4 == 3 else f"at {9 + i % 3} am"
        text = f"Book a site visit for {name} on {day} {when}"
        cases.append(("visits", text))
    return cases
if __name__ == "__main__":
    cases = make_cases()
    print(len(cases), "test inputs")
    for feature in ("listings", "contacts", "visits"):
        mine = [text for f, text in cases if f == feature]
        print(f"{feature:9} {len(mine):2}  e.g. {mine[3]}")
