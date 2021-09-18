# Meta-1.2-Implementar-funciones-que-hagan-uso-de-las-estructuras-de-la-repetici-n-y-selecci-n
1.Impuestos. Una empresa desea calcular la estimación del importe de impuestos que los empleados deben pagar. Los ingresos inferiores a 8.000 euros no están sujetos a impuestos; los comprendidos entre 8.000 euros y 20.000 euros, lo están al 18 %; los comprendidos entre 20.000 euros y 35.000 euros, están sujetos al 27% y los superiores a 35.000 euros, lo están al 38%. Diseña una función impuestos(x) que calcule los impuestos correspondientes a los ingresos x. Entrada: Un valor x de ingresos. Salida: Los impuestos correspondientes a x con 2 decimales.

2.IMC. Diseña una función imc(p,h) que reciba reciba el peso p y la altura h de una persona, calcule el índice de masa corporal de una persona (IMC = peso[kg]/altura²[m]) y retorne el estado en el que se encuentra esa persona en función del valor de IMC: 
<16: criterio de ingreso hospitalario 
de 16 a 17: infrapeso 
de 17 a 18: bajo peso 
de 18 a 25: saludable 
de 25 a 30: sobrepeso 
de 30 a 35: sobrepeso crónico 
de 35 a 40: obesidad premórbida
>40: obesidad mórbida 
Entrada: Peso p y altura h. Salida: Estado.
Ejemplo:
>>> imc(1.65,68)
 'saludable'

3.Número perfecto. Diseñe una función que encuentre el primer número perfecto mayor que 28 (o un número n dado). Un número es perfecto si coincide con la suma de sus divisores (excepto él mismo). Por ejemplo, 28 es perfecto ya que 28 = 1 + 2 + 4 + 7 + 14.
Ejemplo:
	>>> perfecto(28) 
496 
>>> perfecto(500)
8128

4.Triángulo de asteriscos. Escribir una función no productiva triang(n) que, dado un número n, imprime un "triángulo de asteriscos de tamaño n".

5.Es primo?. Diseña una función es_primo(n) que reciba un natural n y devuelva True si el número es primo o False en caso contrario. Se asume que n > 1.
