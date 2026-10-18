# Evals: a tiny eval set, a ROUGE-1 style score, two prompt versions
import re
from mini_llm import call_model, DOCS

def words(s): return re.findall(r"[a-z0-9]+", s.lower())
def rouge1(output, reference):          # shared words, as an F1 score
    out, ref = words(output), words(reference)
    common = sum(min(out.count(w), ref.count(w)) for w in set(ref))
    if common == 0: return 0.0
    recall, precision = common / len(ref), common / len(out)
    return 2 * precision * recall / (precision + recall)

EVAL_SET = [  # question, help page, the answer we expect
    ("When will my refund come?", "refund", "Refund in 5 to 7 working days."),
    ("My UPI payment failed", "upi", "The bank reverses it within 48 hours."),
    ("How long is delivery?", "delivery", "3 to 5 days, metros 2 days."),
    ("Can I pay cash?", "cod", "Cash on delivery up to 10000 rupees.")]

for v in ("v1", "v2"):
    s = [rouge1(call_model("answer", q, prompt=v, context=DOCS[k]), ref)
         for q, k, ref in EVAL_SET]
    print(v, [round(x, 2) for x in s], "mean", round(sum(s) / len(s), 2))
