"""""
DESCRIPCION: Numero perfecto > a 28 o al # introducido
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 17/09/21
"""""

def numeroPerfecto(num):
    n = 1
    suma = 0
    b = False
    c = 1
    numero = 28
    d = False
    cuenta = 0
    numeroPerfectoA = 0
    numeroPerfectoAnt = 0
    nnn = ""

    if num < 27:
        print("Primer número perfecto mayor al {}, es el número {}".format(num, 28))
    else:
        while b == False or d == False:

            if float(numero % n) == 0:
                suma = suma + n
                print("♥")
            n += 1

            if numero == suma and n == numero:
                b = True
                suma = 0
                numeroPerfectoA = numero

            if n > numero and b == False:
                numero += 1
                n = 1
                suma = 0

            if b == True:
                if numero <= num:
                    b = False
                    n = 1
                    suma = 0
                    numero += 1
                    numeroPerfectoAnt = numeroPerfectoA

                else:
                    d = True
                    if numeroPerfectoA > numero:
                        numeroPerfectoA = numeroPerfectoAnt
                    print("Primer número perfecto mayor al {}, es el número {}".format(num, numeroPerfectoA))

num = int(input("INTRODUCE 28 PARA SABER CUAL ES EL # PERFECTO > AL 28 Ó INTRODUCE OTRO # PARA CONOCER EL # PERFECTO MAYOR + CERCANO: "))
numeroPerfecto(num)