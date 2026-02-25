vals = [1231, 124, 1245, 52, 1, 3]

print(len(vals))

def mean(vals):
    total = 0
    for val in vals:
        total += val
    return total / len(vals)

print(mean(vals))