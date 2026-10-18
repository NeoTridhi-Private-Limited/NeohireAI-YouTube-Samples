# Evaluator-optimizer: one call writes, another judges, repeat
from mini_llm import call_model

attempt, feedback = 1, ""
while attempt <= 5:
    draft = call_model("headline", feedback, attempt=attempt)
    verdict = call_model("critique", draft)
    print(f"try {attempt}: {draft!r}\n   critic: {verdict}")
    if verdict == "approve":
        break
    feedback, attempt = verdict, attempt + 1
