"""""
DESCRIPCION: Saber si el numero dado es primo
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

n = int(input("Numero: "))

def es_primo(n):
    b = 0
    i = 2
    primo = True
    while i < n:
        if n%i == 0:
            primo = False
            b = 0
        i = i + 1
    if n <= 1:
        primo = False
    if b != 0:
        primo = True

    return primo

print("Es primo: ",es_primo(n))