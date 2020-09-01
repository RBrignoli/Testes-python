import pytest

def soma_lista(lista, minimo=0):

    maximo = len(lista) - 1
    if maximo == minimo:
        return lista[maximo]
    
    return lista[minimo] + soma_lista(lista, minimo+1)


@pytest.mark.parametrize("entrada, saida",[
    ([1,2,3],6),
    ([4,5,6],15),
    ([-20,64,0],44)
    ])
def testa_soma_lista(entrada, saida):
    assert soma_lista(entrada) == saida
