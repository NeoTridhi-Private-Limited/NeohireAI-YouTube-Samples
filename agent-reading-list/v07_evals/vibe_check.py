# A vibe check: try a few requests by hand. They all look fine.
from mini_llm import call_model, reset
reset()
for text in ["3 BHK in Hyderabad under 90 lakh",
             "Book a site visit for Anita Rao on Sunday at 10 am",
             "2 BHK in Chennai under 60 lakh"]:
    print(">", text)
    print(" ", call_model("reply", text).replace("\n", "\n  "))
