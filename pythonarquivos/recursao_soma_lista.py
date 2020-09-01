
def soma_lista(lista, minimo=0):

    maximo = len(lista) - 1
    if maximo == minimo:
        return lista[maximo]
    
    return lista[minimo] + soma_lista(lista, minimo+1)

