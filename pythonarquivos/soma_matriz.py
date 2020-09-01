def dimensões_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    return(linhas,colunas)

def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz


def soma_matrizes(mat1, mat2):

    a = dimensões_matriz(mat1)
    b = dimensões_matriz(mat2)
    teste = False
    matriz_resultado = []

    if (a[0] == b[0] and a[1] == b[1]):
        teste = True
        for i in range(a[0]):
            linha = []
            for j in range(a[1]):
                linha.append(mat1[i][j] + mat2[i][j])
            matriz_resultado.append(linha)
        return(matriz_resultado)
    else:
        return(teste)

def main():
    matriz_1 = cria_matriz(5,4,2)
    matriz_2 = cria_matriz(5,5,3)
    c = soma_matriz(matriz_1, matriz_2)
    print(c)
    
