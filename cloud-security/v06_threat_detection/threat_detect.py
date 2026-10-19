# Spotting a leaked access key by its behaviour, like a threat detector
BASELINE = {"regions": {"ap-south-1"}, "hours": range(9, 20),
            "calls": {"GetObject", "PutObject"}}
EVENTS = [("10:05", "ap-south-1", "GetObject", 1),
          ("11:40", "ap-south-1", "PutObject", 1),
          ("03:12", "us-east-1", "ListBuckets", 1),
          ("03:14", "us-east-1", "RunInstances", 40),
          ("03:15", "eu-west-1", "RunInstances", 40),
          ("03:20", "us-east-1", "StopLogging", 1)]
for time, region, call, count in EVENTS:
    why = []
    if region not in BASELINE["regions"]: why.append("new region")
    if int(time[:2]) not in BASELINE["hours"]: why.append("odd hour")
    if call not in BASELINE["calls"]: why.append("new call")
    if call == "RunInstances" and count >= 20: why.append("server burst")
    if call == "StopLogging": why.append("logs off")
    level = "HIGH" if len(why) >= 4 else "MEDIUM" if why else "ok"
    tags = ", ".join(why)
    print(f"{time} {region:10} {call:12} x{count:<2} {level:6} {tags}")
