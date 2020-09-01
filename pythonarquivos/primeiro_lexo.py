def primeiro_lex(lista):
    a = ord(lista[0][0])
    index = 0
    for palavra in lista:
        if a > ord(palavra[0]):
                   index = lista.index(palavra)
    return(lista[index])


def main():
    lista = ['Ola', 'c', 'a', 'casa']
    print(primeiro_lex(lista))
    
          
                   
    
