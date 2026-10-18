# Prompt chaining: outline -> check (a gate in code) -> draft
from mini_llm import call_model

def gate(outline):                            # plain code checks the step
    return len(outline.splitlines()) == 3

topic = "UPI refunds"
outline = call_model("outline", topic)
print("Outline:\n" + outline)

if gate(outline):
    print(call_model("draft", outline, topic=topic))
else:
    print("Gate failed: fix the outline before drafting")
