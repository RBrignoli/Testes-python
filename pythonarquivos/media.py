def main():

	cont = 1
	media = 0
	while ( cont <= 4 ):
		entrada = int(input("digite o valor da nota "))
		media = media + entrada
		cont += 1 
	media = media/4
	print("a média aritimética é",media)
		
	
main()