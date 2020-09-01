def insertion_sort(lista):

    for i in range(1, len(lista)):
        index = i
        valor = lista[i]
        while index > 0 and valor < lista[index - 1]:
            print(lista)
            lista[index]  = lista[index-1]
            index -= 1
        lista[index] = valor
    print(lista)
    return lista 
    
