# Building Effective Agents: the working sample

Companion code for the NeoTridhi video on Anthropic's article "Building Effective Agents"
(Erik S. and Barry Zhang, December 2024). The video explains the ideas in our own words; read the original article as well.

Everything runs offline with plain Python 3.10+. A small stand-in model (`mini_llm.py`) answers each call,
so you can see the patterns work without an API key.

| File | Pattern from the article |
|---|---|
| `augmented.py` | the augmented LLM: retrieval, a tool, memory |
| `chain.py` | prompt chaining with a gate in code |
| `router.py` | routing to handlers, and to a small or large model |
| `parallel.py` | parallelization: sectioning and voting |
| `orchestrator.py` | orchestrator-workers: the plan depends on the request |
| `evaluator.py` | evaluator-optimizer: write, judge, repeat |
| `agent.py` | an agent loop with tools and a stopping condition |
| `compounding.py` | why small error rates add up over many steps |
| `poka_yoke.py` | mistake-proofing a tool (absolute paths only) |
| `support_desk.py` + `agent_tools.py` | everything together: a store's support desk |

Run any file:

    python support_desk.py

## Using a real model

Replace the body of `call_model()` in `mini_llm.py` with a call to your provider's API, and turn each
`task` into a prompt (for example task "classify" -> "Classify this message as refund, technical or general").
The other files do not change: that is the point of keeping the model behind one small function.
