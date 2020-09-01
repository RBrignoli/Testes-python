def computador_escolhe_jogada(n, m):
    tn = n - 1
    tm = m
    l = 1
    teste = False
    while teste == False:
        if tn % (tm+1) == 0:
            teste = True
            return(l)
        else:
            if l != tm:
                tn -= 1
                l += 1
            else:
                teste = True
                return(l)
            

def usuario_escolhe_jogada(n, m):

    l = int(input("digite sua jogada: "))
    teste = False
    while teste == False:
        if l > m:
            print("sua jogada foi invalida, tente novamente")
            l = int(input("digite sua jogada: "))
        else:
            return(l)
            teste = True

def partida():
    n = int(input("digite o valor de N (numero de peças): "))
    m = int(input("digite o valor de M (numero maximo para retirada: "))
    a = 2
    jogada = 0
    fim = False
    
    if n % (m+1) == 0:
        print("Você Começa")
        while fim == False:
            if a % 2 == 0:
                jogada = usuario_escolhe_jogada(n, m)
                print("peças antes: ", n," jogada: ", jogada)
                n = n - jogada
                print("peças agora: ", n)
                if n <= 0:
                    fim = True
                    print("Você ganhou!")
                    return(0)
                a  += 1
            else:
                jogada = computador_escolhe_jogada(n, m)
                print("peças antes: ", n," jogada: ", jogada)
                n = n - jogada
                print("peças agora: ", n)
                if n <= 0:
                    fim = True
                    print("O computador ganhou!")
                    return(1)

                a += 1
        
    else:
        print("Computador começa")
        while fim == False:
            if a % 2 == 0:
                jogada = computador_escolhe_jogada(n, m)
                print("peças antes: ", n," jogada: ", jogada)
                n = n - jogada
                print("peças agora: ", n)
                if n <= 0:
                    fim = True
                    print("O computador ganhou!")
                    return(1)

                a  += 1
            else:
                jogada = usuario_escolhe_jogada(n, m)
                print("peças antes: ", n," jogada: ", jogada)
                n = n - jogada
                print("peças agora: ", n)
                if n <= 0:
                    fim = True
                    print("Você Ganhou!")
                    return(0)
                a += 1

def campeonato():
    vencedor = 0
    pc = 0
    jogador = 0
    rodada = 1
    print("Voce Escolheu Campeonato")
    while rodada < 4:
        print("*** Rodada ", rodada,"***")
        partida()
        if vencedor == 1:
           pc +=1
           rodada += 1
        else:
            jogador += 1
            rodada += 1
        print("**** PLACAR: PC ", pc," x Jogador ", jogador,"****")
    if pc >= 2:
        print(" o PC ganhou o torneio")
    else:
        print(" o jogador ganhou o torneio")
        
    



def main():
    teste = False
    escolha = 0
    print("Bem vindo ao NIM! Escolha")
    while teste == False:
        print("1 - para partida isolada ")
        print("2 - para torneio ")
        escolha = int(input())
        if escolha == 1:
            partida()
            teste = True
        elif escolha == 2:
            campeonato()
            teste = True
        else:
            teste = False


main()

