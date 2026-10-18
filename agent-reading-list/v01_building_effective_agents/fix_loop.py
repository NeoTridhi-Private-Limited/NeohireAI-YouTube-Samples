# A coding agent's loop: change the code, run the tests, read the result
def tests(gst):                                   # the "environment": real tests
    cases = [(100, 118), (1000, 1180), (0, 0)]
    return [p for p, want in cases if round(gst(p)) != want]

attempts = [lambda p: p * 18,                     # attempt 1: forgot the base
            lambda p: p + 18,                     # attempt 2: added, not a rate
            lambda p: p * 1.18]                   # attempt 3: price plus 18%
for n, patch in enumerate(attempts, 1):
    failing = tests(patch)
    print(f"attempt {n}: {'all tests pass' if not failing else f'fails for {failing}'}")
    if not failing:
        break
