# One base prompt with policy variables, instead of a prompt per customer type
import textwrap

BASE = ("You help {name} at a bank's call centre. {name} has banked with us "
        "for {tenure} and often asks about {topics}. Start with a warm "
        "hello, reply in {language}, then answer their questions.")

customers = [
    {"name": "Lakshmi", "tenure": "12 years", "topics": "UPI limits",
     "language": "Telugu"},
    {"name": "Arjun", "tenure": "8 months", "topics": "card delivery",
     "language": "Hindi"},
]
for c in customers:
    print(textwrap.fill(BASE.format(**c), 72), end="\n\n")
