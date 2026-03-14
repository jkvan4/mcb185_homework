import gzip
import sys

# ~/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz

def hydropathy(pro):
    aas = 'ACDEFGHIKLMNPQRSTVWY'
    kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
    -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)
    total = 0
    for aa in pro:
        idx = aas.index(aa)
        total += kdh[idx]
    return total / len(pro)

with open(sys.argv[1], 'rt') as fp:
   for line in fp:
        if line[0] != '>': continue
        for i in range(0,30): # SIGNAL 
            win = line[i:i+8]
            if hydropathy(win) >= 2.5: print('signal')
        for j in range(len(fp)-10): # TRANSMEMBRANE
            win = line[j:j+11]
            if hydropathy(win) >= 2.0: print()


