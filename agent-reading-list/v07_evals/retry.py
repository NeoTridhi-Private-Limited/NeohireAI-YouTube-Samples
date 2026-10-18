# Assertions at run time: if a reply fails a check, retry with feedback
from mini_llm import call_model, reset
from checks import CHECKS
reset()

def answer(feature, text, tries=2):
    feedback = ""
    for attempt in range(1, tries + 1):
        reply = call_model("reply", text, feedback=feedback)
        failed = [c.__name__ for c in CHECKS[feature] if not c(reply)]
        print(f"  try {attempt}: {reply.splitlines()[0][:40]}  {failed}")
        if not failed:
            return reply
        feedback = "Fix: " + ", ".join(failed)
    return "Sorry, let me get a person to help."

answer("contacts", "Add Anita Rao, phone 98480 12346")
answer("listings", "3 BHK in Pune under 150 lakh")
