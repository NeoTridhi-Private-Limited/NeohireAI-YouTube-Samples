# A real chain from hiring: extract skills -> gate -> match -> summary
from mini_llm import call_model

resume = "Built REST APIs in Python and SQL, deployed with Docker on AWS."
must_have = "python, sql, docker, kubernetes"

skills = call_model("extract_skills", resume)          # step 1
print("Skills:", skills)
if not skills:                                         # gate: nothing found, stop
    raise SystemExit("No skills found: ask for a better resume")
fit = call_model("match", skills, need=must_have)      # step 2
print("Match:", fit)
print(call_model("summary", fit))                      # step 3
