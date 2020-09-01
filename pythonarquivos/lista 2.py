def remove_repetidos(lista):
    for numero in lista:
        while numero in lista[lista.index(numero)+1:]:
            del lista[lista.index(numero)]
    n=1
    lista.sort()
    return(lista)
            
def main():

    a = 1
    lista = []
    while a != 0:
        a = int(input("digite um numero positivo, para finalizar digite 0: ")) 
        lista.append(a)
        print(lista)
    del lista[lista.index(0)]
    lista = remove_repetidos(lista)
    print (lista)

    
    
