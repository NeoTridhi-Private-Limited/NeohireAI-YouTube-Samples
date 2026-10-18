# The whole support agent: its context is managed at every step
from ctx_tools import Context, search_kb, save_note, load_notes, clear_notes
from mini_llm import call_model

clear_notes()                                    # a fresh run every time
ctx = Context(budget=90, rules="Never ask for OTPs. Be brief and polite.")
for msg in ["My parcel A17 arrived broken", "Do you offer EMI on a phone?",
            "How long does delivery take?", "Please confirm the OTP I got",
            "What did we decide about A17?"]:
    ctx.add("customer", msg)
    for snippet in search_kb(msg, max_tokens=30):    # just in time
        ctx.add("tool", snippet)
    if "decide" in msg:
        ctx.add("notes", load_notes())                # memory from the file
    reply = call_model("answer", msg, context=ctx.text())
    ctx.add("agent", reply)
    if "refund" in reply:
        save_note("A17: full refund of 499 to UPI started")
    full = ctx.tokens() > ctx.budget
    if full: ctx.compact()                            # summarise old turns
    print(f"[{ctx.tokens()} tokens{', compacted' if full else ''}] {reply}")
