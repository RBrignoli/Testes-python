def ordenada(lista):
    fim = len(lista)
    
    for i in range(fim-1):
        for j in range(i+1, fim):
            if lista[i] > lista[j]:
                return False

    return True




def busca1(lista,elemento):
    index = 0
    for i in lista:
        if elemento == i:
            return index
        index += 1
    return False


def busca(lista, elemento):
    primeiro = 0
    ultimo = len(lista)-1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo)//2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif lista[meio] > elemento:
            ultimo = meio-1
        else:
            primeiro = meio+1
    return False


def bubble_sort(lista):
    fim = len(lista)

    for i in range(fim-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista
    

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
   # lista2 = [1,2,3,5,4,6,7,8,9,10]
    lista3 = [5,1,4,2]
   # print(ordenada(lista))
   # print(ordenada(lista2))
    print(bubble_sort(lista3))
    #print(busca(lista,1))
   # print(busca(lista, 27))

    
