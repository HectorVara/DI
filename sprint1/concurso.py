pregunta="""En qué año estamos?
a)2022
b)2021
c)1989

"""

opcion= input(pregunta)
puntos=0
if opcion=="a":
	print("Correcto")
	puntos+=5
elif opcion=="b":
	print("Incorrecto")
	puntos-=5
elif opcion=="c":
	print("Incorrecto")
	puntos-=5
else:
	print("Teclea a,b o c")
pregunta="""En qué año fue el mundial de Francia?
a)2022
b)2021
c)1998

"""
opcion= input(pregunta)

if opcion=="a":
	print("Incorrecto")
	puntos+=5
elif opcion=="b":
	print("Incorrecto")
	puntos-=5
elif opcion=="c":
	print("Correcto")
	puntos-=5
else:
	print("Teclea a,b o c")
	
pregunta="""En qué año fue el mundial de Italia?
a)2022
b)2021
c)1990

"""
opcion= input(pregunta)

if opcion=="a":
	print("Incorrecto")
	puntos-=5
elif opcion=="b":
	print("Incorrecto")
	puntos-=5
elif opcion=="c":
	print("Correcto")
	puntos+=5
else:
	print("Teclea a,b o c")
	
print(str(puntos)+" puntos")
	
