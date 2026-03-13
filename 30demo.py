import sys
import mcb185

seq = 'GACACAGACAGAGACA'

w = int(sys.argv[1])


skew = 0
comp = 0
for i in range(len(seq) -w+1):
    win = (seq[i:i+w])
    g = 0
    c = 0
    for nt in win:
        if nt == 'C': c += 1
        elif nt == 'G': g += 1
    comp += ((g+c) / len(win))
    skew += ((g-c) / (g+c))
    print(win, comp, skew)
print(comp / (i+1))
print(skew / (i+1))