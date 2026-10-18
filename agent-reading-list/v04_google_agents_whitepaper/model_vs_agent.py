# A model alone vs an agent: live data through a tool, memory across turns
from mini_llm import call_model

def fare_tool(route):                       # live data the model never saw
    return {"HYD-BLR": 1450}[route]

history = []                                # the agent keeps the session
def agent(question):
    history.append(question)
    facts = f"route=HYD-BLR fare={fare_tool('HYD-BLR')}"
    chat = " | ".join(history)
    return call_model("agent_answer", f"{facts} {chat} question: {question}")

for q in ["Train fare Hyderabad to Bengaluru today?", "And for two people?"]:
    print("You:  ", q)
    print("Model:", call_model("answer_alone", q))
    print("Agent:", agent(q))
