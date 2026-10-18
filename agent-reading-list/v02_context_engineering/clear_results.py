# Tool result clearing: old raw tool outputs are rarely needed again
from mini_llm import count_tokens

raw = "{status: shipped, hub: Nagpur, scans: [...]} " * 40
history = [("customer", "Where is my parcel A17?"),
           ("tool", "track_parcel A17 -> " + raw),
           ("agent", "It left the Nagpur hub, arriving Friday."),
           ("customer", "And my other order B22?"),
           ("tool", "track_parcel B22 -> " + raw),
           ("agent", "B22 is out for delivery today.")]

def size(h): return sum(count_tokens(text) for _, text in h)
last_tool = max(i for i, (who, _) in enumerate(history) if who == "tool")
cleared = [(who, f"[cleared: {text.split(' ->')[0]} result]")
           if who == "tool" and i != last_tool else (who, text)
           for i, (who, text) in enumerate(history)]
print(f"before: {size(history)} tokens, after: {size(cleared)} tokens")
print("kept the latest tool result, and every message from people")
print(cleared[1])
