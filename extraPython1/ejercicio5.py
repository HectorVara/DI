def suma(lista):
    suma=0
    for i in range(len(lista)):
        suma=lista[i] + suma
    return suma


def mult(lista):
    mult=1
    for i in range(len(lista)):
        mult= lista[i]*mult
    return mult

print (mult([3,2,4]))