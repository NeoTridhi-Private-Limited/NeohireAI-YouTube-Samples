# Level 1 evals: plain assertions, cheap enough to run on every change
import re
UUID = re.compile(r"[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}")

def no_uuid(reply):                       # generic: never show internal IDs
    shown = re.sub(r"\{\{.*?\}\}", "", reply)   # {{...}} becomes a link
    return not UUID.search(shown)

def count_matches(reply):                 # listings: said count == listed
    said = re.search(r"(?:found|Showing) (\d+)", reply)
    return not said or int(said.group(1)) == reply.count("\n- ")

def has_time(reply):                      # a booking needs a time
    return not reply.startswith("Booked") or " at " in reply

CHECKS = {"listings": [no_uuid, count_matches], "contacts": [no_uuid],
          "visits": [no_uuid, has_time]}
if __name__ == "__main__":
    ID = "1b4e28ba-2fa1-11d2-883f-0016d3cca427"
    for r in [f"Added Ravi. Contact ID {ID}", "Added Ravi. {{%s}}" % ID,
              "I found 5 homes:\n- 3 BHK, 82 lakh", "Booked for Sunday."]:
        print(no_uuid(r), count_matches(r), has_time(r), "|", repr(r[:24]))
