# Why word-overlap metrics mislead: short, paraphrased and wrong answers
import re

def words(s): return re.findall(r"[a-z0-9]+", s.lower())

def overlap(output, reference):   # precision (BLEU-like), recall (ROUGE-like)
    out, ref = words(output), words(reference)
    common = sum(min(out.count(w), ref.count(w)) for w in set(ref))
    return common / len(out), common / len(ref)

reference = "Refund in 5 to 7 working days"
outputs = {"too short": "Refund",
           "right, new words": "Your money comes back within a week",
           "wrong numbers": "Refund in 50 to 70 working days"}

for name, out in outputs.items():
    p, r = overlap(out, reference)
    print(f"{name:17} precision {p:.2f}  recall {r:.2f}")
