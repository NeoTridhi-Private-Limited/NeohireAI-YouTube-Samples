# Optimistic execution: the agent starts while a guardrail checks in parallel
from concurrent.futures import ThreadPoolExecutor
from mini_llm import call_model

class TripwireTriggered(Exception): pass

def churn_guardrail(message):
    if call_model("churn_risk", message) == "yes":
        raise TripwireTriggered("churn risk, pass to the retention team")

def handle(message):
    with ThreadPoolExecutor() as pool:
        draft = pool.submit(call_model, "answer", message)  # starts at once
        check = pool.submit(churn_guardrail, message)       # at the same time
    try:
        check.result()
        return "sent: " + draft.result()
    except TripwireTriggered as e:
        return "draft thrown away, " + str(e)

for m in ["How do I return a kurta?", "I think I will cancel my membership"]:
    print(f"{m}\n  {handle(m)}")
