def superposicion(cadena1, cadena2):
    long=0
    if len(cadena1) > len(cadena2):
        long=len(cadena1)
    else:
        long=len(cadena2)

    cont=0
    while (cont < long -1):
        if cadena1[cont]==cadena2[cont]:
            return True
        cont+=1
    return False

print(superposicion("casa", "vaca"))