def main():
	
	import math
	vet = [];
	n = 0;
	while n < 3:	
		vet.append(int(input("digite os parametros a b c")))
		n += 1
	delta = (vet[1]**2) - (4*vet[0]*vet[2])
	if delta < 0:
		print("esta equação não possui raízes reais")
	elif delta == 0:
		raiz = (0-vet[1])/(2*vet[0])
		print("a raiz desta equação é", raiz)
	else:
		raiz1 = ((0-vet[1]) + math.sqrt(delta))/(2*vet[0])
		raiz2 = ((0-vet[1]) - math.sqrt(delta))/(2*vet[0])
		if raiz2 > raiz1:
			print("as raízes da equação são", raiz1,"e", raiz2)
		else:
			print("as raízes da equação são", raiz2,"e", raiz1)
main()