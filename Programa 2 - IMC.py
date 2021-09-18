"""""
DESCRIPCION: Calculo del IMC y reporte de salud
AUTOR: Vara Espinoza Andrea Lizeth
FECHA DE CREACION: 12/09/21
ULTIMA MODIFICACION: 17/09/21
"""""
#formula =  (IMC =peso[kg]/altura²[m])

altura = float(input("INGRESE ALTURA EN M: "))
peso = float(input("INGRESE PESO EN KG: "))
imc = 0

#FUNCION
def CalculoIMC(peso, altura):
    global imc
    imc = (peso) / (altura ** 2)
    if imc <16:
        estado = "Ingreso hospitalario"
    elif imc > 16 and imc <=17:
        estado =" Infrapeso"
    elif imc >=17 and imc <=18:
        estado = "Bajo peso"
    elif imc >= 18 and imc <=25:
        estado = "Saludable"
    elif imc >= 25 and imc <=30:
        estado = "Sobrepeso"
    elif imc >= 30 and imc <=35:
        estado = "Sobrepeso crónico"
    elif imc >=35 and imc <=40:
        estado = "Obesidad premórbida"
    elif imc <40:
        estado = "Obesidad mórbida"
    else:
        estado = "Ingreso no valido"
    return estado


print("Estado: {}\nIMC: {:.2F}".format(CalculoIMC(peso, altura), imc) )