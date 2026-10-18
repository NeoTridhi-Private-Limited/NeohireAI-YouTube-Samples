# Tree-of-Thoughts: explore branches, judge them, back up from dead ends
import operator as op
from itertools import permutations
OPS = {"+": op.add, "-": op.sub, "*": op.mul}
def chain(nums):                  # one chain of thought: the first idea
    path = [f"{sum(nums[:k])}+{nums[k]}={sum(nums[:k+1])}" for k in (1, 2, 3)]
    return path, sum(nums)
def tree(nums, path, seen):       # many thoughts, a judge, backtracking
    if len(nums) == 1:
        return path if nums[0] == 24 else None
    for i, j in permutations(range(len(nums)), 2):
        rest = [n for k, n in enumerate(nums) if k not in (i, j)]
        for s, f in OPS.items():
            v = f(nums[i], nums[j]); seen[0] += 1
            if v < 0: continue    # the judge prunes a hopeless branch
            step = f"{nums[i]}{s}{nums[j]}={v}"
            found = tree(rest + [v], path + [step], seen)
            if found: return found
path, end = chain([4, 9, 10, 13]); seen = [0]
print("One chain:", *path, f"-> {end}, not 24. Stuck.")
print("Tree:", *tree([4, 9, 10, 13], [], seen), f"({seen[0]} thoughts)")
