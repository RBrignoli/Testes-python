class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
            

    def perimetro(self):
        perimetro = self.a + self.b + self.c
        return perimetro

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return ("equilátero")
        elif self.a != self.b != self.c != self.a:
            return ("escaleno")
        else:
            return ("isóceles")

    def retangulo(self):
        lista = [self.a,self.b,self.c]
        lista = sorted(lista)
        quadrado = True
        a=3
        for numero in lista:
            if numero % a == 0:
                a+=1
            else:
                quadrado = False
        return quadrado


    def semelhantes(self, triangulo):
       a = self.tipo_lado()
       b = triangulo.tipo_lado()
       if a == b:
           return True
       else:
           return False
