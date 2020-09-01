def imprime_matriz(matriz):

    for i in matriz:
        for c in i:
            print (c, end='')
        print()
        

def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def main():
    matriz = cria_matriz(5,5,0)
    imprime_matriz(matriz)
