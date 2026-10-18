# LLM Powered Autonomous Agents: the working sample

Companion code for the NeoTridhi video on Lilian Weng's post "LLM Powered Autonomous Agents"
(Lil'Log, June 2023). The video explains the ideas in our own words; read the original post as well.

Everything runs offline with plain Python 3.10+, standard library only. A small scripted stand-in model
(`mini_llm.py`) answers each call, so you can watch the patterns work without an API key. Outputs are deterministic.

| File | Idea from the post |
|---|---|
| `decompose.py` | task decomposition: model prompting, a task-specific template, human input |
| `cot.py` | chain of thought: steps instead of a direct guess |
| `tot.py` | Tree of Thoughts: keep the best few partial plans at each level |
| `llm_p.py` | LLM+P: the model translates, a classical planner (breadth-first search) plans |
| `react.py` | ReAct: Thought, Action, Observation in a loop |
| `reflexion.py` | Reflexion: a repeat-detecting heuristic, a stored lesson, success on retry |
| `memory_window.py` | short-term memory is the context window: old turns fall out |
| `vector_store.py` | long-term memory: facts as vectors, found by maximum inner product |
| `lsh.py` | nearest neighbour search: brute force vs locality-sensitive hashing |
| `mrkl.py` | MRKL: a router sends questions to expert modules (calculator, weather table) |
| `hugginggpt.py` | HuggingGPT: plan, select a model, execute, respond |
| `api_bank.py` | API-Bank idea: retrieve the right API, then call it |
| `memory_stream.py` | Generative Agents: recency + importance + relevance retrieval |
| `parse_output.py` | the fragile natural-language interface: insisting on valid JSON |
| `agent_main.py` + `agent_parts.py` | everything together: plan, remember, use tools, reflect |

Run any file from this folder:

    python agent_main.py

## Using a real model

Replace the body of `call_model()` in `mini_llm.py` with a call to your provider's API, and turn each
`task` into a prompt (for example task "subgoals" -> "Break this goal into 3-5 short subgoals, separated by ->").
The other files do not change. `tot.py`, `lsh.py`, `memory_window.py`, `vector_store.py`, `api_bank.py` and
`memory_stream.py` need no model at all: they are the plain algorithms the post describes.
