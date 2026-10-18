# A Practical Guide to Building Agents: the working sample

Companion code for the NeoTridhi video on OpenAI's guide "A practical guide to building agents" (2025).
The video explains the ideas in our own words; read the original guide as well.

Everything runs offline with plain Python 3.10+. A small stand-in model (`mini_llm.py`) answers each call,
and `agent_kit.py` holds an online store's orders, typed tools, specialist agents and the run loop,
so you can see the ideas work without an API key.

| File | Idea from the guide |
|---|---|
| `when_to_build.py` | a rules engine next to judgment: UPI fraud review |
| `models.py` | baseline with a large model, then try a small one per task, with evals |
| `tool_types.py` | data, action and orchestration tools, one standard definition |
| `instructions.py` | turning an existing help article into a clear routine with edge cases |
| `run_loop.py` | the run loop and its exit conditions: final answer, error, turn limit |
| `templates.py` | one base prompt with policy variables |
| `tool_overlap.py` | tool overload comes from overlap: find tools that look alike |
| `manager.py` | manager pattern: specialist agents called as tools |
| `handoff.py` | decentralized pattern: triage hands off to orders, refunds, sales |
| `guardrails.py` | layered guardrails: length limit, blocklist, safety and relevance classifiers |
| `pii_filter.py` | checking the model's reply for personal data before it is sent |
| `tool_risk.py` | rating each tool low, medium or high risk |
| `optimistic.py` | the agent works while a guardrail checks in parallel (a tripwire) |
| `human.py` | handing to a person: failure threshold, high-risk action |
| `store_desk.py` | everything together: a store's support desk |

Helpers: `mini_llm.py` (the stand-in model) and `agent_kit.py` (tools, agents, run loop).
`store_desk.py` also imports `guardrails.py` and `pii_filter.py`.

Run any file from this folder:

    python store_desk.py

## Using a real model

Replace the body of `call_model()` in `mini_llm.py` with a call to your provider's API, and turn each
`task` into a prompt (for example task "intent" -> "Classify this message as orders, refunds, technical or sales").
For agents, give the model each tool's name and description and ask it to choose the next step.
The other files do not change: that is the point of keeping the model behind one small function.
All order numbers, phone numbers and the card number are made up (4111 1111 1111 1111 is a standard test number).
