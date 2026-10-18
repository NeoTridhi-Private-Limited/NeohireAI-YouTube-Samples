# Hybrid: a short rules file always goes in, everything else on demand
from mini_llm import count_tokens, call_model

RULES = "Never ask for OTPs. Refunds over 5000 need a manager."  # always
FAQ = {"delivery": "Metro cities get delivery in 2 days.",
       "emi": "EMI is available on orders above 3000.",
       "exchange": "Exchanges are free within 10 days."}
def search_faq(question):                       # loaded just in time
    return [v for k, v in FAQ.items() if k in question.lower()]

for q in ["Can I pay by EMI for a 4000 phone?", "Please confirm my OTP"]:
    context = RULES + " " + " ".join(search_faq(q))
    reply = call_model("answer", q, context=context)
    print(f"> {q}\n  [{count_tokens(context)} tokens] {reply}")
