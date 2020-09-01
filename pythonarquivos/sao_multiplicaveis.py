
def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz

def sao_multiplicaveis(m1,m2):

    linhas1 = len(m1[0])
    colunas2 = len(m2)
    Teste = False

    if linhas1 == colunas2:
        Teste = True
    return Teste
        
        

def main():
    
    matriz1 = cria_matriz(1,1,0)
    matriz2 = cria_matriz(1,3,1)
    a = sao_multiplicaveis(matriz1, matriz2)
    print (a)
