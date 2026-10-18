# The augmented LLM: a model plus retrieval, a tool and memory
from mini_llm import call_model, KB

memory = []                                   # what the assistant remembers

def search_kb(question):                      # retrieval
    return [v for k, v in KB.items() if k in question.lower()]

def assistant(question):
    facts = search_kb(question)
    memory.append(question)
    reply = call_model("answer", question + " " + " ".join(facts))
    return reply, len(memory)

print(assistant("When will my refund arrive?"))
print(assistant("My UPI payment failed, what now?"))
