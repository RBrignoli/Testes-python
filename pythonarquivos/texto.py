import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    cont = 0
    somatorio = 0
    while cont <= 5:
        somatorio = somatorio + abs(as_a[cont] - as_b[cont])
        grau_de_similaridade = somatorio/6
        cont += 1 
    print(grau_de_similaridade)
    return(grau_de_similaridade)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    tamanho_total_palavras = 0
    tamanho_total_sentença = 0
    tamanho_total_frase = 0
    frases = []
    palavras = []
    
    sentenças = separa_sentencas(texto)
    
        
    for sentença in sentenças:
        frases = frases + separa_frases(sentença)
        tamanho_total_sentença = tamanho_total_sentença + len(sentença)
            
    for frase in frases:
        palavras = palavras + separa_palavras(frase)
        tamanho_total_frase = tamanho_total_frase + len(frase)

    for palavra in palavras:
        tamanho_total_palavras = tamanho_total_palavras + len(palavra)


             
                
    tmp = tamanho_total_palavras / len(palavras)
    rtt = n_palavras_diferentes(palavras) / len(palavras)
    rhl = n_palavras_unicas(palavras) / len(palavras)
    tms = tamanho_total_sentença / len(sentenças)
    cds = len(frases) / len(sentenças)
    tmf = tamanho_total_frase / len(frases)

    
    return (tmp , rtt , rhl, tms, cds, tmf)
        

def avalia_textos(textos, ass_cp):
    provavel_copiah = 9999
    assinaturas_textos = []
    comparaçoes = []
    for texto in textos:
        assinaturas_textos.append(calcula_assinatura(texto))
    for assinatura in assinaturas_textos:
        comparaçoes.append(compara_assinatura(ass_cp, assinaturas_textos[assinaturas_textos.index(assinatura)]))
    for comparaçao in comparaçoes:
        if provavel_copiah > comparaçao:
            provavel_copiah = comparaçao
    provavel_copiah = comparaçoes.index(provavel_copiah) + 1 

    return(provavel_copiah)


def main():
    assinatura_lida = le_assinatura()
    textos = le_textos()
    copiah = avalia_textos(textos, assinatura_lida)
    
    listas = teste()
    copiah = avalia_textos(listas[1], listas[0])
    print('O autor do texto', copiah, ' esta infectado com COPIAH')
    
    
    
    
def teste():
    ass = [4.72, 0.72, 0.56, 80.5, 2.5, 31.6]
    textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.',
              'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
              'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    print(ass)
    print(textos)

    return(ass, textos)
    
