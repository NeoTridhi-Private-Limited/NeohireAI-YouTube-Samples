# Why raw agreement can lie: when almost everything is good
human = ["good"] * 95 + ["bad"] * 5           # 100 traces, 5 real failures
lazy = ["good"] * 100                          # a judge that always says good
careful = ["good"] * 92 + ["bad"] * 7 + ["good"]   # 3 false alarms, 1 miss

def score(judge):
    pairs = list(zip(human, judge))
    agree = sum(h == j for h, j in pairs) / len(pairs)
    caught = sum(h == j == "bad" for h, j in pairs)
    flagged = judge.count("bad")
    prec = caught / flagged if flagged else 0
    return f"agree {agree:.0%}  caught {caught} of 5  precision {prec:.0%}"

print("lazy judge   ", score(lazy))
print("careful judge", score(careful))
