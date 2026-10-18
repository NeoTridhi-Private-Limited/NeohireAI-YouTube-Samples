# The WaveNet idea: fuse letters in pairs, then pairs of pairs, like a tree
window = ".deepika"                   # eight letters of context

level, step = list(window), 0
print("flat MLP squeezes all at once:", "[" + window + "]")
while len(level) > 1:
    level = [level[i] + level[i + 1] for i in range(0, len(level), 2)]
    step += 1
    print(f"tree layer {step}:", " ".join("[" + g + "]" for g in level))
print("each layer only ever combines two neighbours")
