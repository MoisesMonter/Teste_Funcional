
class Poligono():

    def is_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a


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

    def identificar_triangulo(self,a,b,c):
        y = True if (int(a)+int(b)>int(c) and int(b)+int(c)>int(a) and int(c)+int(a)>int(b)) else False
        return y