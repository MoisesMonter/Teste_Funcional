
class Poligono():

    def um_triangulo(self,a,b,c):
        return a + b > c and a + c > b and b + c > a

    def soma_angulos_internos(self,a,b,c):
        som = a + b + c
        return som == 180
    
    def todos_angulos_zero(self,a,b,c):
        return (a == 0 and b ==0 and c == 0)
    
    def acima_de_zero(self,a,b,c):
        return (a != 0 and b !=0 and c != 0)
    
    def menor_soma_all_divisao(self, a, b, c):
        total = a + b + c
        return (a < float(total / 2) and b < float(total / 2) and c < float(total / 2))

    def lado_igual_soma(self,a,b,c):
        return (a == b+c or b == a+c or c == a+b)

