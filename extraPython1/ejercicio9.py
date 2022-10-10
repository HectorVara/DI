def generar_n_caracteres(n,c):
    resultado=""
    for i in range(n):
        resultado=resultado + c

    return resultado

print(generar_n_caracteres(5,"e"))