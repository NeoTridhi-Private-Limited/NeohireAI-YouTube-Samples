# Decentralized pattern: triage hands off, and the specialist takes over
from mini_llm import call_model
from agent_kit import AGENTS

def converse(message, max_turns=6):
    agent, history = AGENTS["triage"], [f"user: {message}"]
    for _ in range(max_turns):
        step = call_model("next_step", "\n".join(history), agent=agent.name)
        if step.startswith("handoff "):
            print(f"{message:40} triage hands off to {step[8:]}")
            agent = AGENTS[step[8:]]       # control moves, with the history
        elif step.startswith("final "):
            return f"  {agent.name} agent to customer: {step[6:]}"
        else:
            name, arg = step.split(maxsplit=1)
            history.append(f"{name} -> {agent.tools[name](arg)}")
    return "  handing over to a person"

for m in ["Where is my order A17?", "My cooker C31 came damaged, refund it",
          "Any offers on school bags?"]:
    print(converse(m))
