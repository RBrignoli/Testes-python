def main():

    a = 1
    lista = []
    while a != 0:
        a = int(input("digite um numero positivo, para finalizar digite 0: ")) 
        lista.append(a)
        print(lista)
    b = len(lista) - 1
    while b != -1:
        print(lista[b], ", ")
        b -= 1

