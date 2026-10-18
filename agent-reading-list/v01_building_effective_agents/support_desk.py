# The whole support desk: every pattern from the article working together
from concurrent.futures import ThreadPoolExecutor
from mini_llm import call_model
import agent_tools as tools

def handle(message):
    with ThreadPoolExecutor() as pool:                     # parallel: guard + route
        safe = pool.submit(call_model, "guard", message)
        kind = pool.submit(call_model, "classify", message)
    if safe.result() == "unsafe":
        return "Please never share card numbers or OTPs. A person will call you."
    if kind.result() == "refund":                          # routing -> agent
        return tools.refund_agent(message)
    return call_model("answer", message)                   # simple path: one call

for msg in ["My parcel A17 arrived broken, I want a refund",
            "How long does delivery take in metro cities?",
            "Refund please, my card number is 4111 1111"]:
    print(f"> {msg}\n  {handle(msg)}")
