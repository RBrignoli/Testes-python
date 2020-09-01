a= 1
while a > 0:
    a = int(input("numero"))
    i=2
    while a % i != 0:
        i += 1
    if a == i:
        print("é primo")
    else:
        print("não e primo")
