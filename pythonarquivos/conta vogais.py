def conta_letras(frase, contar='vogais'):
    numero = 0
    frase.replace(' ', '')
    numero = frase.count('a')+ frase.count('e')+ frase.count('i')+ frase.count('o')+ frase.count('u')
    tamanho = len(frase)
    if contar == 'vogais':
        return(numero)
    else:
        
        return(tamanho - numero)
                     
