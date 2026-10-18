# Your AI Product Needs Evals: the working sample

Companion code for the NeoTridhi video on Hamel Husain's article "Your AI Product Needs Evals"
(March 2024, hamel.dev/blog/posts/evals/). The video explains the ideas in our own words; read the original article as well.

The sample is an evaluation system for the AI assistant of a property app: it finds homes, adds contacts to a CRM
and books site visits. Everything runs offline with plain Python 3.10+. A small stand-in model (`mini_llm.py`)
plays the assistant. Version 1 has three deliberate bugs (it leaks internal contact IDs, its listing count does
not match what it shows, and it books visits without a time); version 2 fixes them. The evals find them.

| File | Idea from the article |
|---|---|
| `vibe_check.py` | a few requests tried by hand: everything looks fine |
| `checks.py` | level 1: assertions (no UUIDs in replies, count matches the list, a booking has a time) |
| `cases.py` | synthetic test inputs from templates (48 requests) |
| `scoped_tests.py` | scoped tests for one feature: one match, many matches, no match |
| `create_lookup.py` | create a contact, then look it up: exactly one result expected |
| `harness.py` | helper: runs every case through the assistant and the checks, keeps a trace of each |
| `run_tests.py` | pass rate per feature, and which checks fail most |
| `traces.py` | logging traces as JSON lines (in memory) |
| `viewer.py` | a tiny trace viewer that filters to failures |
| `labels.py` | helper: 20 human labels (good or bad) with short critiques |
| `judge.py` | a model as judge, compared with the human labels |
| `align_judge.py` | the judge aligned with human critiques: agreement, precision and recall |
| `imbalance.py` | why raw agreement misleads when almost everything is good |
| `retry.py` | assertions at run time: retry with feedback |
| `fix_and_rerun.py` | fix the bugs, re-run the same tests, compare pass rates |
| `ab_test.py` | level 3: a tiny A/B test with stable assignment (simulated outcomes) |
| `finetune_data.py` | the eval system as a data engine for fine-tuning |
| `evals_main.py` | everything together: evaluate, find the biggest problem, fix, ship at a target |

Run any file from this folder:

    python evals_main.py

## Using a real model

Replace the bodies of `_reply()` and `_judge()` in `mini_llm.py` with calls to your provider's API.
For the judge, write the human critiques from `labels.py` into its prompt, and keep measuring its agreement
with people. The tests, the trace log and the viewer do not change.
