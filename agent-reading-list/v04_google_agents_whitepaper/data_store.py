# A Data Store: documents become vectors; a question finds the closest ones
from store import DOCS, INDEX, search, vector, cosine

question = "How many weeks of leave do I get after my baby is born?"
q = vector(question)
print("Question words:", dict(q))
for name in DOCS:
    print(f"  {name:15} similarity {cosine(q, INDEX[name]):.2f}")
print("Best match:", search(question)[0])
