# HuggingGPT: plan tasks, pick a model for each, run them, then reply
from mini_llm import call_model

MODELS = {"speech-to-text": ["asr-general", "asr-hindi"],
          "translation": ["translate-hi-en"],
          "summarization": ["summarizer-small"]}

request = "A customer left a Hindi voice note. What do they want?"
tasks = call_model("plan_tasks", request)                  # 1. plan
out = {}
for t in tasks:
    model = call_model("pick_model", t["type"],
                       options=MODELS[t["type"]])          # 2. select
    data = out.get(t["dep"], t.get("arg"))                 # dependency
    out[t["id"]] = call_model("run", data, model=model)    # 3. execute
    print(f"{t['id']}. {t['type']:<14} {model:<16} -> {out[t['id']]}")
print("reply:", call_model("respond", out[tasks[-1]["id"]]))  # 4. respond
