def maior_elemento(lista):
    a=0
    for numero in lista:
        if a<numero:
            a = numero
    return (a)
