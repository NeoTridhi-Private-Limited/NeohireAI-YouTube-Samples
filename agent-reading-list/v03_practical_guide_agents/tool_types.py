# Three kinds of tools, each with one standard definition
from agent_kit import Tool, TOOLS

check_pincode = Tool(                # a new tool: the same shape as the rest
    name="check_pincode", kind="data",
    description="Say if we deliver to a PIN code, e.g. 560001",
    fn=lambda pin: "we deliver here" if pin[0] in "56" else "not yet")
TOOLS[check_pincode.name] = check_pincode

for kind in ("data", "action", "orchestration"):
    for t in TOOLS.values():
        if t.kind == kind:
            print(f"{kind:14}{t.name:16}{t.description}")
print("check_pincode('560001') ->", check_pincode("560001"))
