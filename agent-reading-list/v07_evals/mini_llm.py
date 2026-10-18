"""mini_llm.py - a tiny stand-in for the AI assistant of a property app, so every sample runs offline, for free.

call_model("reply", text, version=1) answers an agent's request. Version 1 has three deliberate bugs:
  - it shows internal contact IDs (UUIDs) in its replies,
  - it says how many homes it found, but lists only three,
  - it books a site visit without a time.
Version 2 is the fixed assistant. call_model("query", text) turns a request into a CRM query.
call_model("judge", reply, version=1) is a stand-in critic model; version 2 follows rules written from human critiques.
To use a real model, replace the bodies with API calls (see README.md); the samples do not change.
"""
import re
import uuid

LISTINGS = [  # city, bedrooms, price in lakh rupees
    ("Pune", 2, 52), ("Pune", 2, 58), ("Pune", 2, 74), ("Pune", 3, 82), ("Pune", 3, 86),
    ("Pune", 3, 88), ("Pune", 3, 95), ("Pune", 3, 120), ("Pune", 3, 135),
    ("Hyderabad", 2, 48), ("Hyderabad", 2, 55), ("Hyderabad", 2, 66), ("Hyderabad", 2, 72),
    ("Hyderabad", 3, 78), ("Hyderabad", 3, 99),
    ("Bengaluru", 2, 68), ("Bengaluru", 2, 85), ("Bengaluru", 3, 125), ("Bengaluru", 3, 140),
    ("Chennai", 2, 57), ("Chennai", 3, 92), ("Chennai", 3, 118),
]
SEED_CONTACTS = [("Ravi Kumar", "98765 43210")]   # already in the CRM before the tests run
CONTACTS = []


def reset():
    """Start every test run from the same CRM state."""
    CONTACTS.clear()
    for name, phone in SEED_CONTACTS:
        _add(name, phone)


def _add(name, phone):
    cid = str(uuid.uuid5(uuid.NAMESPACE_DNS, name + phone))   # deterministic ID
    CONTACTS.append({"name": name, "phone": phone, "id": cid})
    return cid


def search(q):
    """The CRM runs the query: plain code, not the model."""
    hits = [(b, p) for c, b, p in LISTINGS
            if c == q["city"] and b == q["bedrooms"] and p < q["max_price"]]
    return sorted(hits, key=lambda h: h[1])


def lookup(name):
    return [c for c in CONTACTS if c["name"] == name]


def _query(text):
    m = re.search(r"(\d) BHK in (\w+) under (\d+) lakh", text)
    return {"city": m.group(2), "bedrooms": int(m.group(1)), "max_price": int(m.group(3))}


def _reply(text, version):
    if "BHK" in text:                                   # the listing finder
        homes = search(_query(text))
        n = len(homes)
        if n == 0:
            return "I found 0 homes."
        head = f"Showing 3 of {n} homes:" if version > 1 and n > 3 else f"I found {n} homes:"
        return head + "".join(f"\n- {b} BHK, {p} lakh" for b, p in homes[:3])
    if text.startswith("Add "):                         # create a contact
        m = re.match(r"Add (.+?), phone (.+)", text)
        cid = _add(m.group(1), m.group(2))
        tag = "{{contact:" + cid + "}}" if version > 1 else f"Contact ID {cid}"
        return f"Added {m.group(1)}. {tag}"
    if text.startswith("Book"):                         # book a site visit
        m = re.search(r"for (.+?) on (\w+)(?: at (.+))?", text)
        name, day, time = m.groups()
        if time:
            return f"Booked a visit for {name} on {day} at {time}."
        if version > 1:
            return f"Which time on {day} works for {name}?"
        return f"Booked a visit for {name} on {day}."
    return "Sorry, I can help with homes, contacts and site visits."


def _judge(reply, version):
    if version == 1:            # an unaligned critic: only checks it looks friendly and complete
        return ("bad", "too short") if len(reply) < 20 else ("good", "clear and polite")
    shown = re.sub(r"\{\{.*?\}\}", "", reply)           # version 2: rules from human critiques
    if re.search(r"[0-9a-f]{8}-[0-9a-f]{4}-", shown):
        return ("bad", "shows an internal contact ID")
    said = re.search(r"(?:found|Showing) (\d+)", reply)
    if said and int(said.group(1)) != reply.count("\n- "):
        return ("bad", "the count does not match the list")
    if reply.startswith("Booked") and " at " not in reply:
        return ("bad", "a booking with no time")
    return ("good", "accurate and complete")


def call_model(task, text="", version=1, feedback=""):
    """One model call. task says what is asked; text is the input."""
    if feedback:                    # told what went wrong, the model corrects itself
        version = 2
    if task == "reply":
        return _reply(text, version)
    if task == "query":
        return _query(text)
    if task == "judge":
        return _judge(text, version)
    raise ValueError(f"unknown task {task}")
