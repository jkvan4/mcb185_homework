X = [1, 2, 4, 3, 5, 6]

def stats(X):
    m = 0
    #mean
    for number in X[0:]:
        m += float(number)
    mean = m / (len(X))
    print('Mean:', mean)
    #stdev
    a = 0
    for stdv in X[0:]:
        a += ((float(stdv) - mean)**2)
        b = ((a / (len(X) - 1))**0.5)
    print('Standard Deviation:', b)
    #median
    X.sort()
    c = (len(X) / 2)
    if len(X) % 2 != 0:
        print('Median:', X[int(c-0.5)])
    else: 
        print('Median:', (float(X[int(c)]) + float(X[int(c-1)])) / 2)
    return '---Stats---'

print(stats(X))