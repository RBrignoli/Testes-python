

def encontra_impares(lista):
    lista2 = []
    if len(lista) > 0:
        numero = lista.pop(0)

        if numero % 2 == 1:
            lista2.append(numero)
            lista2.extend(encontra_impares(lista))
        else:
            lista2.extend(encontra_impares(lista))
    return lista2
            
    
