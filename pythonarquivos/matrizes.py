def dimensoes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    print(str(linhas)+'X'+str(colunas))
    

def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz
    
def main():
    a = cria_matriz(5,5,0)
    dimensoes(a)
