import matplotlib.pyplot as plt

x = [1,2,3]
y = [3,4,3]

# titulo
plt.title("aqui vai o titulo")
#eixos
plt.xlabel("nome do eixo x")
plt.ylabel("nome do eixo y")

plt.plot(x,y)
plt.show()

#grafico de barras
plt.title("titulo")
plt.xlabel("eixo x")
plt.ylabel("eixo y")
plt.bar(x,y)
plt.show()

#comparando 2 graficos de barras

x1 = [1,3,5,7,9]
y1 = [5,2,4,7,3]

x2 = [2,4,6,8,10]
y2 = [6,1,3,6,4]

titulo = "nome do grafico"
eixoX = "nome do eixo x"
eixoY = "nome do eixo y"

# legenda
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label = "Grupo 2")
plt.legend()

#plt.show()
plt.savefig("figura1.pdf")
