import random
def savingthrow(dc, r):
	for i in range(r):
		c = random.randint(1,20)
		print(c)
		if c >= dc: print('Safe!')
		else: print('Fail!')
	return ' '

print(savingthrow(10, 1))
