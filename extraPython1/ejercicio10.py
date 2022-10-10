def histograma(lista):

    for i in range(len(lista)):
        elemento=""
        for j in range(len(lista[i])):
            elemento=elemento+"*"
        print(elemento)

print(histograma(["casa","portatil","clase de dam2"]))