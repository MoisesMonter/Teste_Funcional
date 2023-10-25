from src.poligono.poligono import Poligono
import pytest

test = Poligono()

teste_soma_divizao_2= [(60,50,70,True),(95,45,40,False)]
lados_iguais_asoma = [(90,30,60,True),(50,0,20,False)]


@pytest.mark.parametrize("x,y,z,expected",teste_soma_divizao_2)
def teste_menor_soma_all_divisao(x,y,z,expected):
    if test.um_triangulo(x,y,z):
        print(test.um_triangulo(x,y,z))
        info = test.menor_soma_all_divisao(x,y,z)
        assert info == expected

@pytest.mark.parametrize("x,y,z,expected",lados_iguais_asoma)
def teste_lado_igual_som(x,y,z,expected):
    if test.um_triangulo(x,y,z):
        info = test.lado_igual_soma(x,y,z)
        assert info == expected