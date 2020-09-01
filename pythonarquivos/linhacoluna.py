def main():

    a= int(input("linha: "))
    b= int(input("coluna: "))
    c = 1
    while c <= b:
        d = 1
        while d <= a:
            print("#", end='')
            d += 1
        c += 1
        print("")
main()
