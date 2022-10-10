def max_de_tres(a,b,c):
	if a>b and a>c:
		return a
	elif b>c:
		return b
	return c

print(max_de_tres(3,5,8))