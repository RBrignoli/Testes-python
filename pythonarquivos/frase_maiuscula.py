def maiusculas(frase):
    cont = 0
    frase_maiuscula = ''
    for letra in frase:
        if (ord(letra) > 65 and ord(letra) < 90):
            frase_maiuscula = frase_maiuscula + letra
    return(frase_maiuscula)
