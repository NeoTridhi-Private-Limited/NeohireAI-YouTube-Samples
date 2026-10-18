# A small autonomous agent: plan, remember, use tools, reflect
from mini_llm import call_model
from agent_parts import Memory, TOOLS

memory = Memory()
memory.add("customer Kavya prefers replies in Hindi")
memory.add("order A17 is a phone with a cracked screen")
goal = "Kavya wants a replacement for her cracked phone"
lessons = []

for sub in call_model("subgoals", goal).split(" -> "):       # planning
    facts = memory.recall(sub)                                # memory
    tool, arg = call_model("route", f"{sub} {facts}")         # tool use
    result = TOOLS[tool](arg)
    if result.startswith("error"):                            # reflection
        print(f"{sub:<21} {tool}({arg}) -> {result}")
        lessons.append(call_model("reflect", result))
        tool, arg = call_model("route", f"{sub} {lessons[-1]}")
        result = TOOLS[tool](arg)
    memory.add(f"{sub}: {result}")
    print(f"{sub:<21} {tool}({arg}) -> {result}")
print("lesson kept:", lessons[0])
