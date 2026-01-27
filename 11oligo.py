def oligotm(A, C, G, T):
	x = A+T+G+C
	s = (((A+T)*2) + ((G+C)*4))
	l = 64.9 + (41*(G+C-16.4)/(A+T+G+C))
	if x <= 13: print('Oligo Melting Temperature:', s)
	elif x > 13: print('Oligo melting Temperature:', l)



print(oligotm(1, 1, 1, 1))


