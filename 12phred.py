def char_to_prob(x):
	a = (ord(x))
	b = (a - 33)
	c =  10**(-b/10)
	return c

print(char_to_prob('?'))

import math

def prob_to_char(y):
	d = (((math.log10(y)) * -10) + 33)
	e = int(d)
	f = chr(e)
	return f

print(prob_to_char(0.001))
