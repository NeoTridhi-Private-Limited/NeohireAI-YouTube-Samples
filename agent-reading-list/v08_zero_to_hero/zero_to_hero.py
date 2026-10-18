# The whole course in one run: each lesson file runs, we keep its key line
import io, os, runpy, sys
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
LESSONS = [("micrograd", "grad_check.py", 0), ("neuron", "neuron.py", 2),
           ("bigram", "bigram.py", 1), ("MLP data", "mlp_context.py", 6),
           ("batchnorm", "activations.py", 1),
           ("backprop ninja", "manual_backprop.py", 1),
           ("WaveNet", "wavenet_tree.py", 2), ("GPT", "attention.py", 6),
           ("tokenizer", "bpe.py", 4)]

for title, file, keep in LESSONS:
    buf = io.StringIO()
    with redirect_stdout(buf):
        runpy.run_path(os.path.join(sys.path[0], file), run_name="__main__")
    print(f"{title:>14} | {buf.getvalue().splitlines()[keep].strip()}")
