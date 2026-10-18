# Neural Networks: Zero to Hero, the working sample

Companion code for the NeoTridhi video on Andrej Karpathy's free lecture series
"Neural Networks: Zero to Hero" (https://karpathy.ai/zero-to-hero.html). The video explains the course and
its core ideas in our own words. This code is written fresh for the video and is NOT the course's code:
watch the lectures and build along with them for the real thing.

Everything is pure Python 3.10+ (standard library only, no numpy or torch), offline and deterministic
(fixed random seeds).

| File | Idea (and the lecture it belongs to) |
|---|---|
| `micrograd_lite.py` | helper: a tiny scalar autograd `Value` with +, *, tanh and backward (micrograd) |
| `names_data.py` | helper: thirty two Indian first names, the training set (makemore) |
| `value_demo.py` | a shop bill as a graph; backward() gives every gradient |
| `grad_check.py` | autograd matches a numerical derivative |
| `neuron.py` | one neuron learns a rule with gradient descent |
| `bigram_counts.py` | counting letter pairs |
| `bigram.py` | a bigram model: sample new names, average negative log likelihood |
| `smoothing.py` | why an unseen pair makes the loss infinite, and the fix |
| `mlp_context.py` | building training examples from a three-letter context (MLP) |
| `splits.py` | train, dev and test splits; loss on unseen names is higher |
| `activations.py` | tanh saturation and the batch-norm idea (activations and batchnorm) |
| `manual_backprop.py` | the chain rule by hand matches autograd (backprop ninja) |
| `wavenet_tree.py` | fusing context in pairs, like a tree (WaveNet) |
| `attention.py` | one self-attention step, with and without the causal mask (GPT) |
| `bpe.py` | a toy byte pair encoding tokenizer with encode/decode round trip (tokenizer) |
| `zero_to_hero.py` | runs every lesson file and prints its key line |

Run any file from this folder:

    python zero_to_hero.py

## Credit

These toy files are our own short versions, written for the video, of ideas taught in Andrej Karpathy's
course. `micrograd_lite.py` follows the design of his [micrograd](https://github.com/karpathy/micrograd), and the
lesson files follow the order of [makemore](https://github.com/karpathy/makemore),
[nanoGPT](https://github.com/karpathy/nanoGPT) and [minbpe](https://github.com/karpathy/minbpe),
all released by Andrej Karpathy under the MIT License (Copyright (c) Andrej Karpathy). Please learn from the originals.
