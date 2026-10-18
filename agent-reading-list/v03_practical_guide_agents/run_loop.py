# The run loop: one agent, its tools, and three ways to stop
from mini_llm import call_model
from agent_kit import TOOLS

def run(message, max_turns=2):
    history = [f"user: {message}"]
    for turn in range(1, max_turns + 1):
        step = call_model("next_step", "\n".join(history))
        if step.startswith("final "):              # exit 1: a final answer
            return f"  turn {turn}: final answer, {step[6:]}"
        name, arg = step.split(maxsplit=1)
        if name not in TOOLS:                      # exit 2: an error
            return f"  turn {turn}: error, there is no tool {name}"
        result = TOOLS[name](arg)
        print(f"  turn {turn}: {name}({arg}) -> {result}")
        history.append(f"{name} -> {result}")
    return f"  stopped: reached {max_turns} turns"   # exit 3: the turn limit

for msg in ["Where is my order A17?", "Cancel order A17",
            "Keep checking order C99 until it moves"]:
    print(msg); print(run(msg))
