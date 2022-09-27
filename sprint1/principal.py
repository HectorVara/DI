import time
from fibonacci2 import funcion_fibonacci2
from Fibonacci import funcion_fibonacci
print("""Qué método desea usar?
a) Fibonacci
b) Fibonacci2""")
opcion=input("Opción: ")
if opcion=="a":
	numero=input("Introduzca número: ")
	start_time=time.time()
	print(funcion_fibonacci(int(numero)))
	end_time=time.time()
	elapsed_time=end_time-start_time
	print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
	
elif opcion=="b":
	numero=input("Introduzca número: ")
	start_time=time.time()
	print(funcion_fibonacci2(int(numero)))
	end_time=time.time()
	elapsed_time=end_time-start_time
	print('El tiempo de ejecución ha sido :' + str(elapsed_time) + ' s')
