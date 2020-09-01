n = int(input("digite um numero inteiro: "))
a = 2
b = True
while a != n and b:
    l = n % a
    if l == 0:
        print("não primo")
        b = False
    a += 1
if b:
    print("primo")
    
