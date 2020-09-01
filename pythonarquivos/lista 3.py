def remove_repetidos(lista):
    for numero in lista:
        while numero in lista[lista.index(numero)+1:]:
            del lista[lista.index(numero)]
    n=1
    lista.sort()
    return(lista)
            


    

    
    
