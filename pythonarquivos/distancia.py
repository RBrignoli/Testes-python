def main():
	
	import math
	vet = [];
	n = 0;
	while n < 4:	
		vet.append(int(input("digite as duas coordenadas xy")))
		n += 1
	dx = (vet[0] - vet[2])**2;
	dy = (vet[1] - vet[3])**2;
	dxy = math.sqrt(dx + dy);
	if dxy >= 10:
		print("longe");
	else: 
		print("perto");
main()
