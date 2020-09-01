def menor_nome(lista_nomes):
    menor_nome = lista_nomes[0]
    for nome in lista_nomes:
        nome = nome.strip()
        if len(nome)  < len(menor_nome):
            menor_nome = nome
    menor_nome = menor_nome.capitalize()

    return(menor_nome)

def main():
    lista_nomes = ['maria', '   josé  ', 'paulo', 'catarina']
    a = menor_nome(lista_nomes)
    print(a)
        
