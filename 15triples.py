def triples(x):
	a = 0
	b = 0
	for a in range(1,x):
		for b in range(1,x):
			c = (a**2 + b**2)**0.5
			if c % 1 == 0 and a <= b: print(a,b,c, sep='	')

print(triples(100))


