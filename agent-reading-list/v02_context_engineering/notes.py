# Structured notes: the agent saves progress to a file outside its context
import json, tempfile
from pathlib import Path

RESUMES = [f"R{i:03d}" for i in range(1, 301)]        # 300 resumes to screen
def good_fit(rid): return int(rid[1:]) % 37 == 0      # stand-in for the model

with tempfile.TemporaryDirectory() as folder:
    notes_file = Path(folder) / "NOTES.json"
    for session in range(1, 4):                     # each one: fresh context
        notes = (json.loads(notes_file.read_text()) if notes_file.exists()
                 else {"done": 0, "shortlist": []})     # 1. read the notes
        batch = RESUMES[notes["done"]:notes["done"] + 100]
        notes["shortlist"] += [r for r in batch if good_fit(r)]
        notes["done"] += len(batch)
        notes_file.write_text(json.dumps(notes))        # 2. write them back
        print(f"session {session}: screened {notes['done']}, "
              f"shortlist {len(notes['shortlist'])}")
print("final shortlist:", ", ".join(notes["shortlist"]))
