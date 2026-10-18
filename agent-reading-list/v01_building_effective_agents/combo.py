# Patterns combine: route each resume by role, then run that role's chain
from mini_llm import call_model

MUST = {"backend": "python, sql, docker", "frontend": "react, typescript"}

def role_of(resume):                                   # routing
    return "frontend" if "react" in resume.lower() else "backend"

def screen(resume):                                    # a chain per route
    role = role_of(resume)
    skills = call_model("extract_skills", resume)
    if not skills:                                     # gate
        return f"{role}: no skills found, ask for more detail"
    return f"{role}: " + call_model("match", skills, need=MUST[role])

for r in ["Python and SQL APIs, shipped with Docker",
          "Built React screens in TypeScript",
          "Hardworking and punctual"]:
    print(screen(r))
