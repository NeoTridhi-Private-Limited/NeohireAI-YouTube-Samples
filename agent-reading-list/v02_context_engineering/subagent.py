# Sub-agents: each explores in its own clean context, returns a short summary
from mini_llm import count_tokens, call_model

QUESTIONS = ["why UPI refunds fail", "which couriers damage most parcels",
             "top reasons for returns"]

def sub_agent(question):                 # its own window, thrown away after
    reading = f"Search results and documents about {question}. " * 900
    return count_tokens(reading), call_model("summarise_research", question)

lead_context = 0
for q in QUESTIONS:
    used, summary = sub_agent(q)
    lead_context += count_tokens(summary)
    print(f"sub-agent read {used:,} tokens, returned: {summary}")
print(f"the lead agent's context grew by only {lead_context} tokens")
