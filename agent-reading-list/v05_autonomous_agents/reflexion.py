# Reflexion: fail, write down the lesson, then try again
from mini_llm import call_model

def env(action):                                   # binary reward: 1 or 0
    if action == "pay BL-204": return "paid", 1
    if action == "find_bill electricity": return "bill id is BL-204", 0
    return "error: unknown bill 204", 0

lessons = []                                       # kept across trials
for trial in (1, 2):
    seen = []
    for step in range(4):
        action = call_model("act", " ".join(lessons), step=step)
        obs, reward = env(action)
        if seen and seen[-1] == (action, obs):     # heuristic: a repeat
            print(f"trial {trial}: repeated '{action}', stop"); break
        seen.append((action, obs))
        print(f"trial {trial}: {action} -> {obs}")
        if reward: break
    if reward: break
    lessons = (lessons + [call_model("reflect", str(seen))])[-3:]
    print("lesson:", lessons[-1])
