def inverte_lista(lista):
    lista1=[]
    lista1= lista[len(lista)::-1]
    for numero in lista1:
        print (numero)
        
                    
        
def main():

    a = 1
    lista = []
    while a != 0:
        a = int(input("digite um numero positivo, para finalizar digite 0: ")) 
        lista.append(a)
    del lista[lista.index(0)]
    inverte_lista(lista)
    
main()
