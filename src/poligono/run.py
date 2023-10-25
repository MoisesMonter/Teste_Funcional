from fake import Poligono

if __name__ == "__main__":
    id = Poligono()
    a,b,c = 50,60,70
    print(str(a+b+c),end =' ')
    if id.soma_angulos_internos(a,b,c):
        print("é um poligono")
    else:
        print("não é um poligono")
