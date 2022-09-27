from fibonacci2 import funcion_fibonacci2
from Fibonacci import funcion_fibonacci
print("""Qué método desea usar?
a) Fibonacci
b) Fibonacci2""")
opcion=input("Opción: ")
if opcion=="a":
	numero=input("Introduzca número: ")
	print(funcion_fibonacci(int(numero)))
elif opcion=="b":
	numero=input("Introduzca número: ")
	print(funcion_fibonacci2(int(numero)))
