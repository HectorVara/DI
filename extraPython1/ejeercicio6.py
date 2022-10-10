def inversa(cadena):
    cont=1
    invertida=""
    while cont < len(cadena)+1:
        invertida=invertida+cadena[len(cadena)-cont]
        cont+=1

    return invertida

print(inversa("python"))