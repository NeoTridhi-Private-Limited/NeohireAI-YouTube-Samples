# Effective Context Engineering: the working sample

Companion code for the NeoTridhi video on Anthropic's article "Effective context engineering for AI agents"
(Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield, Anthropic's Applied AI team, 29 September 2025).
The video explains the ideas in our own words; read the original article as well.

Everything runs offline with plain Python 3.10+. A small stand-in model (`mini_llm.py`) answers each call,
counts tokens with a rough rule (about 4 characters per token) and has a toy "context rot" curve.
The numbers it prints are for teaching, not measurements of any real model.

| File | Idea from the article |
|---|---|
| `tokens.py` | a token budget: what fills the context window |
| `pairs.py` | why long context is costly: every token attends to every other |
| `rot.py` | context rot, a toy simulation: more text, less recall |
| `tool_choice.py` | overlapping tools confuse the model; a clean tool set does not |
| `few_shot.py` | a few diverse, canonical examples instead of many similar ones |
| `select_snippets.py` | choosing which retrieved snippets go in, within a budget |
| `just_in_time.py` | keep file names, load only the files the task needs |
| `peek.py` | head, tail and search on a big log instead of loading it |
| `hybrid.py` | a short rules file always in, everything else on demand |
| `compaction.py` | summarise old turns, keep decisions and open items |
| `clear_results.py` | tool result clearing: drop old raw tool outputs |
| `notes.py` | structured note-taking: progress saved to a file across context resets |
| `subagent.py` | sub-agents explore in their own context and return short summaries |
| `support_agent.py` + `ctx_tools.py` | everything together: a store's support agent with a managed context |

Run any file:

    python support_agent.py

`notes.py` writes its notes file in a temporary folder that is removed afterwards;
`support_agent.py` keeps its notes in your temp folder (`support_agent_NOTES.md`) and clears them at the start of each run.

## Using a real model

Replace the body of `call_model()` in `mini_llm.py` with a call to your provider's API, and replace
`count_tokens()` with the provider's token counter. Turn each `task` into a prompt (for example task
"summarise" -> "Summarise this conversation. Keep every decision and every open item."). The other files do not change.
