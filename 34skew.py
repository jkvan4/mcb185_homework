import sys

seq = sys.argv[1]
w = int(sys.argv[2])

for i in range(len(seq) -w+1):
    win = (seq[i:i+w])
    g = win.count('G')
    c = win.count('C')
    if g+c != 0: skew = ((g-c) / (g+c))
    else: skew = 0
    print(win, skew,sep='     ')

