n = int(input("digite um numero inteiro: "))
res = 0
while n != 0:
    a = n % 10
    n = n // 10
    res = a + res
print (res)
