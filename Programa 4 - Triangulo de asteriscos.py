"""""
DESCRIPCION: Triangulo con *
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

numero =int(input("DAME UN NUMERO "))

def  triang(numero):
    i = 1
    suma = 0

    while i <= numero:
        print("*"*i)
        i+=1


triang(numero)