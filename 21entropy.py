import math

probs = [0.5, 0.4, 0.1]

sum = 0
for p in probs: sum += p

if not math.isclose(sum, 1.0):
    print('error! :( probs must add up to 1.0)')
else: print('yay!')

