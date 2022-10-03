def funcion_fibonacci(n):
	if n==0:
		return 0
	if n==1:
		return 1
	if n>1:
		return funcion_fibonacci(n-1) + funcion_fibonacci(n-2)
