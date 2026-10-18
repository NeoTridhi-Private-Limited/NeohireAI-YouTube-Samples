"""mini_llm.py - a tiny stand-in for a language model, so every sample runs anywhere, offline, for free.

Each call names a task ("subgoals", "route", ...) and the stand-in answers the way a well-behaved model would.
It is scripted, not intelligent: it exists so you can watch the agent patterns work without an API key.
To use a real model, replace the body of call_model() with an API call (see README.md); the samples do not change.
"""
import re

def call_model(task, text="", **kw):
    """One model call. task says what is asked; text is the input."""
    t = text.lower()
    if task == "subgoals":                          # task decomposition
        if "replacement" in t:
            return "check the order -> check the policy -> book the replacement -> tell the customer"
        if kw.get("style"):
            return "Checklist: stock, prices, banners, payments, delivery slots"
        return "pick the products -> set the discounts -> test UPI checkout -> announce the sale"
    if task == "solve":                             # chain of thought vs a direct guess
        n, price, coupon, delivery = map(int, re.findall(r"\d+", text))
        if not kw.get("think"):
            return f"{n * price} rupees"            # the classic shortcut: stops after the first step
        a = n * price
        return (f"{n} x {price} = {a}\n{a} - {coupon} = {a - coupon}\n"
                f"{a - coupon} + {delivery} = {a - coupon + delivery} rupees")
    if task == "to_pddl":                           # LLM+P: natural language -> a planning problem
        return "(:init (at box store)) (:goal (at box ward3))"
    if task == "from_plan":                         # LLM+P: plan -> natural language
        stops = text.split()
        return f"Take the box from the {stops[0]} via the {' and the '.join(stops[1:-1])}, to {stops[-1]}."
    if task == "react":                             # ReAct: returns (thought, action, argument)
        if "search_policy" not in t:
            return "I need the refund rule first.", "search_policy", "refund"
        if "order_age" not in t:
            return "Now I need when A17 was delivered.", "order_age", "A17"
        return "4 days is inside the 7 day window.", "finish", "Yes, A17 can still be refunded."
    if task == "act":                               # Reflexion: the actor reads past lessons
        if "find_bill" in t:
            return ["find_bill electricity", "pay BL-204"][min(kw.get("step", 0), 1)]
        return "pay 204"
    if task == "reflect":                           # Reflexion: turn a failure into a lesson
        if "unknown bill" in t:
            return "Paying '204' failed twice. Next time, find_bill first to get the full id."
        if "order id" in t:
            return "Use the order id, like A17, not the product name."
        return "No lesson needed."
    if task == "route":                             # MRKL-style router: returns (expert, argument)
        m = re.search(r"(\d+) (times|plus|minus) (\d+)", t)
        if m:
            return "calculator", f"{m.group(1)} {dict(times='*', plus='+', minus='-')[m.group(2)]} {m.group(3)}"
        if "weather" in t:
            return "weather", next(c for c in ("chennai", "shimla", "pune") if c in t)
        if t.startswith("check the order"): return "lookup_order", "A17"
        if t.startswith("check the policy"): return "search_policy", "replacement"
        if t.startswith("book the replacement"):
            return "book_replacement", "A17" if "order id" in t else "phone"
        if t.startswith("tell the customer"): return "reply", "Hindi" if "hindi" in t else "English"
        return "llm", t.rstrip("?.").replace("write a ", "").split(" for ")[0]
    if task == "write":
        return "Thank you for every parcel, rain or shine."
    if task == "plan_tasks":                        # HuggingGPT stage 1
        return [{"id": 1, "type": "speech-to-text", "dep": None, "arg": "voice_note.wav"},
                {"id": 2, "type": "translation", "dep": 1},
                {"id": 3, "type": "summarization", "dep": 2}]
    if task == "pick_model":                        # HuggingGPT stage 2
        opts = kw["options"]
        return next((o for o in opts if "hindi" in o), opts[0])
    if task == "run":                               # HuggingGPT stage 3 (the expert models)
        model = kw["model"]
        if model.startswith("asr"): return "mera parcel toota hua aaya, replacement chahiye"
        if model.startswith("translate"): return "my parcel came broken, I want a replacement"
        return "wants a replacement for a broken parcel"
    if task == "respond":                           # HuggingGPT stage 4
        return f"Customer {text}."
    if task == "agent_json":                        # an agent that must reply in JSON
        return ['Sure! Here is my plan: I will check the order.',
                '{"thoughts": "check the order first"}',
                '{"command": {"name": "lookup_order", "args": {"id": "A17"}}}'][kw.get("attempt", 1) - 1]
    raise ValueError(f"unknown task {task}")
