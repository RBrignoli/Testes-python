#crescimento populacional teste 1980 - 2016 DATASUS
import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines() #abre os dados

x = [] #cria vetores que vao separar os dados em duas colunas
y = []

for i in range(len(dados)): #navega nos dados
    if i != 0: #elimina a linha 0 pois só contem o cabeçalho e nao interessa
        linha = dados[i].split(";") #separa os dados em duas colunas. separas pelo ;
        x.append(int(linha[0])) #coleta x
        y.append(int(linha[1])) #coleta y


#plotando os graficos e testando variações
plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color="k", linestyle="--")

plt.title("Crescimento pop. 1980-2016")
plt.xlabel("Ano")
plt.ylabel("Pop")
#plt.show()
plt.savefig("pop-brasileira.png", dpi=300)