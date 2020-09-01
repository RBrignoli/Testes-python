def main():

    a= int(input("coluna: "))
    b= int(input("linha: "))
    e = 1
    c = 1
    while c <= b:
        d = 1
        while d <= a:
            if d == 1 or c == 1 or c == b or d == a:
                print("#", end='')
            else:
                print(" ", end='')
            d += 1
        c += 1
        print("")
main()
