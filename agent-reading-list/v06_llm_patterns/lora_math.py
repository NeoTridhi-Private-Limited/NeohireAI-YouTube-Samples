# Why LoRA is cheap: train two thin matrices instead of the whole layer
d = 4096                                   # one layer: a 4096 x 4096 matrix
full = d * d
print(f"full fine-tuning of one layer: {full:,} numbers")
for r in (8, 16, 64):                      # LoRA rank
    lora = d * r + r * d                   # A is d x r, B is r x d
    print(f"LoRA rank {r:2}: {lora:,} numbers, {lora / full:.2%} of it")

# QLoRA also stores the frozen base model in 4 bits instead of 16
params = 7e9                               # a 7 billion parameter model
for bits in (16, 4):
    gb = params * bits / 8 / 1e9
    print(f"7B model weights at {bits:2} bits: {gb:.1f} GB")
