# Patterns for Building LLM-based Systems & Products: the working sample

Companion code for the NeoTridhi video on Eugene Yan's article "Patterns for Building LLM-based Systems & Products"
(July 2023, eugeneyan.com/writing/llm-patterns). The video explains the ideas in our own words; read the original article as well.

Everything runs offline with plain Python 3.10+ (standard library only). A small stand-in model (`mini_llm.py`) answers each call,
including a few typical mistakes, so you can see each pattern catch something real without an API key.
The running example is an online store's help desk: refunds, failed UPI payments, delivery and cash on delivery.

| File | Pattern from the article |
|---|---|
| `eval_overlap.py` | evals: a tiny eval set and a ROUGE-1 style score comparing two prompt versions |
| `metric_limits.py` | why overlap metrics mislead: short, paraphrased and wrong answers |
| `judge_bias.py` | LLM-as-judge: swap the order, count only agreed wins (position and length bias) |
| `hybrid_retrieval.py` | RAG retrieval: keyword score + "embedding" cosine, blended |
| `lora_math.py` | fine-tuning: how few numbers LoRA trains, and what 4-bit (QLoRA) saves |
| `cache_exact.py` | caching: exact keys versus normalised keys, and the hit rate |
| `cache_keys.py` | why semantic caching can serve the wrong answer; an item ID key cannot |
| `guard_json.py` | output guardrail: JSON schema check with retries |
| `guard_pii.py` | output guardrails: PII redaction, blocklist, length cap |
| `defensive_ux.py` | defensive UX: confidence thresholds, sources, and fallbacks |
| `feedback.py` | user feedback: explicit thumbs plus implicit actions, satisfaction per topic |
| `finetune_data.py` | the data flywheel: rated answers become fine-tuning examples |
| `assistant.py` | everything together: cache, retrieval, model, guardrails, logging |

`mini_llm.py`, `hybrid_retrieval.py`, `guard_pii.py` and `defensive_ux.py` are also imported by other files; keep them in the same folder.

Run any file:

    python assistant.py

## Using real components

- Model: replace the body of `call_model()` in `mini_llm.py` with your provider's API call, and turn each `task` into a prompt.
- Embeddings: replace `embed()` in `mini_llm.py` with a real embedding model, and `keyword()` with BM25.
- Evals: keep `eval_overlap.py`'s eval set growing from real questions; add an LLM judge for open-ended answers.

The other files do not change: that is the point of keeping the model behind one small function.
