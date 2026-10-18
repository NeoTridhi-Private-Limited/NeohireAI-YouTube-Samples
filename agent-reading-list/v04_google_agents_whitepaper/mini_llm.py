"""mini_llm.py - a tiny stand-in for a language model, so every sample runs anywhere, offline, for free.

Each call names a task ("react", "fill_args", ...) and the stand-in answers the way a well-behaved model would.
It is deliberately simple and scripted: it shows the SHAPE of what a real model returns (a ReAct step, a
function call as JSON, an answer grounded in retrieved text), not real intelligence.
To use a real model, replace the body of call_model() with an API call (see README.md); the samples do not change.
"""
import json, re

STOP = set("a an the of to for in on at is are am be i my me you your we our it this that and or "
           "do does did can could please what how many much when where which who with after up get "
           "may by from will would should instead".split())

def words(text):
    """Lower-case words without the very common ones."""
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]

CITY = {"hyderabad": "HYD", "bengaluru": "BLR", "chennai": "MAA", "pune": "PNQ", "delhi": "DEL"}

def call_model(task, text="", **kw):
    """One model call. task says what is asked; text is the input. Returns a string."""
    t = text.lower()

    if task == "decide":                     # three_parts.py: pick the next step, or finish
        if "track_order" not in t:
            return "track_order " + re.search(r"\b([A-Z]\d+)\b", text).group(1)
        mins = re.search(r"(\d+) min", t).group(1)
        return f"finish Your order is out for delivery, about {mins} minutes away."

    if task == "answer_alone":               # a model with no tools and no history
        if "two" in t:
            return "Two tickets for which trip? I only see this one message."
        return "About 1200 rupees, from my training data. It may be out of date."

    if task == "agent_answer":               # the same model, given tool results and history
        fare = int(re.search(r"fare=(\d+)", t).group(1))
        people = 2 if "two" in t.split("question:")[-1] else 1
        who = "two people" if people == 2 else "one person"
        return f"{people * fare} rupees for {who}, at today's fare."

    if task == "react":                      # react_loop.py: one Thought / Action step
        if "observation" not in t:
            return "Thought: I need live trains, not my memory.\nAction: search_trains[HYD-BLR]"
        if "check_seats" not in t:
            budget = int(re.search(r"under (\d+)", t).group(1))
            ok = [n for n, p in re.findall(r"(t\d+) 3a (\d+)", t) if int(p) < budget]
            return f"Thought: {ok[0].upper()} fits the budget. Check seats.\nAction: check_seats[{ok[0].upper()}]"
        train = re.search(r"check_seats\[(t\d+)\]", t).group(1).upper()
        seats = re.search(r"(\d+) seats", t).group(1)
        price = re.search(train.lower() + r" 3a (\d+)", t).group(1)
        return f"Thought: I have what I need.\nFinal Answer: {train}, {price} rupees, {seats} seats left."

    if task == "direct":                     # cot.py: answer at once (and slip, like models often do)
        n = [int(x) for x in re.findall(r"\d+", text)]
        return f"{n[0] + n[1] - (n[0] + n[1]) * n[2] // 100}"
    if task == "cot":                        # cot.py: think step by step
        consult, tests, pct = [int(x) for x in re.findall(r"\d+", text)]
        covered = tests * pct // 100
        return (f"Step 1. Insurance pays {pct}% of tests only, {covered}.\n"
                f"Step 2. Patient pays {tests} - {covered} = {tests - covered} for tests.\n"
                f"Step 3. Plus consultation {consult}. Answer {consult + tests - covered}.")

    if task == "fill_args":                  # extension.py: fill the API's parameters, guided by examples
        get = lambda p: (re.search(p, text, re.I) or [None, None])[1]
        return json.dumps({"origin": get(r"from ([A-Z]\w+)"), "destination": get(r"to ([A-Z]\w+)"),
                           "date": get(r"on (\d+ \w+)")})

    if task == "function_call":              # function_call.py: propose a call, as JSON, run nothing
        dish = next((d for d in ("dosa", "biryani", "idli", "thali") if d in t), "thali")
        price = re.search(r"under (\d+)", t)
        return json.dumps({"name": "show_restaurants", "args": {
            "dish": dish, "veg": "veg" in t.split(), "max_price": int(price.group(1)) if price else None}})

    if task == "pay_proposal":               # client_side.py: propose a UPI payment, never make it
        amount = int(re.search(r"(\d+) rupees", t).group(1))
        payee = re.search(r"to ([A-Z]\w+ [A-Z]\w+)", text).group(1)
        return json.dumps({"name": "pay_upi", "args": {"to": payee, "amount": amount}})

    if task == "rag_answer":                 # rag.py: answer only from the retrieved text
        context, source = kw.get("context"), kw.get("source")
        if not context:
            return "I couldn't find that in our policies. Please ask HR."
        return f"{context.split('. ', 1)[1]} (source: {source})"

    if task == "pick_tool":                  # learning.py: copy the label of the closest example in the prompt
        examples = kw["examples"]
        overlap = [len(set(words(text)) & set(words(ex))) for ex, _ in examples]
        return examples[overlap.index(max(overlap))][1]

    if task == "concierge":                  # concierge.py: ReAct over a data store, an extension and a function
        seen = t.count("observation:")
        if seen == 0:
            return "Thought: Check the travel policy first.\nAction: policy[train class limit]"
        if seen == 1:
            cities = [CITY[c] for c in re.findall(r"\b(" + "|".join(CITY) + r")\b", t.split("\n")[0])]
            return f"Thought: Policy checked. Search live trains.\nAction: trains[{'-'.join(cities)}]"
        if seen == 2:
            cap = int(re.search(r"up to (\d+) rupees", t).group(1))
            fits = [(int(p), n) for n, p in re.findall(r"(t\d+) 3a (\d+)", t) if int(p) <= cap]
            price, train = min(fits)
            return f"Thought: {train.upper()} is 3A at {price}, within policy.\nAction: book_ticket[{train.upper()}]"
        if "booked" in t:
            pnr = re.search(r"pnr (\d+)", t).group(1)
            train = re.search(r"book_ticket\[(t\d+)\]", t).group(1).upper()
            return f"Final Answer: Booked {train} for Friday, PNR {pnr}."
        return "Final Answer: You declined, so nothing was booked."

    raise ValueError(f"unknown task {task}")
