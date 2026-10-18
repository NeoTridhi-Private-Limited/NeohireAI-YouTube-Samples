# RAG: retrieve the best document, then answer ONLY from it
from mini_llm import call_model
from store import DOCS, search

def answer(question, min_score=0.2):
    score, name = search(question)[0]
    if score < min_score:                        # nothing relevant: say so
        return call_model("rag_answer", question, context=None)
    return call_model("rag_answer", question, context=DOCS[name], source=name)

for q in ["How many weeks of leave after my baby is born?",
          "How many sick days do I get?",
          "What is the dress code on Fridays?"]:
    print(">", q, "\n ", answer(q))
