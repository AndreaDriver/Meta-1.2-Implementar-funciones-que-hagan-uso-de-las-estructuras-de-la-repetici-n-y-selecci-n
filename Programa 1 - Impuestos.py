"""""
DESCRIPCION: Calculo de estimación del importe de impuestos
que los empleados deben pagar dependiendo de sus ingresos
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
#PREGUNTA DE INGRESOS
valorX = float(input("INGRESA IMPORTE: "))


#DEFINICIO DEL METODO
def impuestoCalculo (valorX):
    if valorX <8000.00:
        impuesto = 0
    elif valorX >= 8000 and valorX <=20000:
        impuesto = valorX*.18
    elif valorX >20000 and valorX <= 35000:
        impuesto = valorX*.27
    elif valorX >35000:
        impuesto = valorX*.38
    return impuesto

print("EL IMPUESTO CORRESPONDIENTE ES: {:.2f}".format(impuestoCalculo(valorX)))