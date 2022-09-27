import random
pregunta1="""En qué año estamos?
a)2022
b)2021
c)1989

"""
pregunta2="""En qué año fue el mundial de Francia?
a)2022
b)2021
c)1998

"""
pregunta3="""En qué año fue el mundial de Italia?
a)2022
b)2021
c)1990

"""
puntos=0
Preguntas=[pregunta1,pregunta2,pregunta3]
cont=2
while cont>0:
	indice=random.randint(0,cont)
	opcion= input(Preguntas[indice])
	if indice==0:
		Preguntas.pop(indice)
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
			
	if indice==1:
		Preguntas.pop(indice)
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
	
	if indice==2:
		Preguntas.pop(indice)
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
		
	cont-=1
	

	
print(str(puntos)+" puntos")
	
