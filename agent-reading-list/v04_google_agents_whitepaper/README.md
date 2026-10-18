# Google's "Agents" whitepaper: the working sample

Companion code for the NeoTridhi video on Google's whitepaper "Agents"
(Julia Wiesinger, Patrick Marlow and Vladimir Vuskovic, Google, September 2024). The video explains the ideas
in our own words; read the original whitepaper as well (it is shared on Kaggle).

Everything runs offline with plain Python 3.10+. A small stand-in model (`mini_llm.py`) answers each call,
so you can see the ideas work without an API key. The stand-in is scripted: it shows the *shape* of what a
real model returns (a ReAct step, a function call as JSON, an answer grounded in retrieved text).

| File | Idea from the whitepaper |
|---|---|
| `three_parts.py` | an agent = model + tools + orchestration layer |
| `model_vs_agent.py` | a model alone vs an agent: live data and session memory |
| `react_loop.py` | ReAct: Thought, Action, Observation, repeated |
| `cot.py` | Chain-of-Thought: intermediate steps fix a wrong quick answer |
| `tot.py` | Tree-of-Thoughts: explore branches, prune, backtrack |
| `brittle.py` | hand-written glue code that breaks on a missing detail |
| `extension.py` | an Extension: example + required parameters, called agent-side |
| `function_call.py` | a Function: the model proposes JSON, the app runs it |
| `client_side.py` | why Functions: the app keeps the keys, the limits and the consent |
| `data_store.py` + `store.py` | a data store: word-count vectors and cosine similarity |
| `rag.py` | retrieval-augmented generation, with an honest "not found" |
| `learning.py` | targeted learning: fixed examples vs retrieved examples |
| `concierge.py` + `travel_tools.py` | everything together: a company travel desk |

Run any file:

    python concierge.py

## Using a real model

Replace the body of `call_model()` in `mini_llm.py` with a call to your provider's API, and turn each
`task` into a prompt (for example task "react" -> "Answer in the format Thought / Action / Observation").
For `function_call.py`, declare `show_restaurants` as a function (tool) to the model; the model returns its
name and arguments, and your code runs it, exactly as here. In `store.py`, swap the word counts for real
embeddings and the loop for a vector database. The other files do not change.
