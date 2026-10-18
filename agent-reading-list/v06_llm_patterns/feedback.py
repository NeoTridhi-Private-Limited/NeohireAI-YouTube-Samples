# Collect feedback: explicit thumbs, implicit actions, one number per topic
from collections import defaultdict

LOG = [  # (topic, what the user did)
    ("refund", "thumbs_up"), ("refund", "copied"), ("refund", "thumbs_up"),
    ("upi", "thumbs_down"), ("upi", "asked_again"), ("upi", "thumbs_up"),
    ("delivery", "thumbs_up"), ("delivery", "copied"), ("upi", "to_human"),
    ("cod", "thumbs_down"), ("cod", "thumbs_up"), ("delivery", "asked_again")]
SIGNAL = {"thumbs_up": 1, "copied": 1,            # explicit and implicit good
          "thumbs_down": 0, "asked_again": 0, "to_human": 0}   # and bad

score = defaultdict(list)
for topic, action in LOG: score[topic].append(SIGNAL[action])
explicit = [SIGNAL[a] for _, a in LOG if a.startswith("thumbs")]
print(f"thumbs only: {sum(explicit)}/{len(explicit)} happy")
for topic, s in sorted(score.items(), key=lambda kv: sum(kv[1]) / len(kv[1])):
    print(f"{topic:9} satisfied {sum(s) / len(s):.0%} ({len(s)} signals)")
