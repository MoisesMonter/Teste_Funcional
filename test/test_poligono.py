from src.poligono.poligono import Poligono
import pytest

test = Poligono()

teste_poligono =        [(50,60,70,True),(30,30,30,False)]
teste_acima_de_zero = [(134,2,4,True),(3,0,1,False)]
teste_poligono_zero =   [(0,0,0,True)   ,(3,0,3,False)]

@pytest.mark.parametrize("x,y,z,expected",teste_poligono)
def teste_poligono(x,y,z,expected):
    if test.um_triangulo(x,y,z):
        info = test.soma_angulos_internos(x,y,z)
        assert info == expected

@pytest.mark.parametrize("x,y,z,expected",teste_acima_de_zero)
def teste_poligono_sem_zero(x,y,z,expected):
    if test.um_triangulo(x,y,z):
        info = test.acima_de_zero(x,y,z)
        assert info == expected

@pytest.mark.parametrize('x,y,z,expected',teste_poligono_zero)
def teste_poligno_zeros(x,y,z,expected):
    if test.um_triangulo(x,y,z):
        info = test.todos_angulos_zero(x,y,z)
        assert info == expected

