def main():

	vet = [];
	n=0;
	while n < 3:
		vet.append(int(input("digite um numero ")))
		n += 1;
	if(vet[0] < vet[1] and vet[1] < vet[2]):
		print("crescente");
	else:
		print("não esta em ordem crescente");
main()