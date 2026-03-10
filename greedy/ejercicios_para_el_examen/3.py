"""
Una empresa de transporte tiene un camión con capacidad limitada de carga (capacity). Debes transportar una selección de n objetos, cada uno con:

val[i]: el valor asociado al objeto.
wt[i]: el peso del objeto.
📌 Restricciones:

No se puede exceder la capacidad total de la mochila.
A diferencia del problema clásico de 0/1 Knapsack, aquí puedes tomar fracciones de un objeto.
🎯 Objetivo: Determinar el valor máximo total que se puede obtener llenando la mochila.

📥 Entrada
val[]: arreglo de enteros que representa el valor de cada objeto.
wt[]: arreglo de enteros que representa el peso de cada objeto.
capacity: entero que representa la capacidad máxima de la mochila.
📤 Salida
Un número real que representa el valor máximo total alcanzable, permitiendo tomar objetos completos o fracciones.
✅ Ejemplos
Ejemplo 1 val = [60, 100, 120] wt = [10, 20, 30] capacity = 50 Salida: 240

Explicación:

Tomamos los objetos de 10kg y 20kg completos.
Tomamos 2/3 del objeto de 30kg.
Valor total = 60 + 100 + (2/3 × 120) = 240.
"""

def mochilla(capacidad= int, valor =[],peso =[]):
    contador_valor = 0
    contador_peso =0
    for i in range(len(valor)):
        contador_valor += valor[i]
        contador_peso += peso[i]

        if contador_peso > capacidad:
            contador_valor -= valor[i]
            contador_peso -= peso[i]
            restante = capacidad - contador_peso
            fraccion = restante / peso[i]
            contador_valor += valor[i]*fraccion
            return contador_valor
        elif contador_peso == capacidad:
            return contador_valor 
    return contador_valor

valor = [60,100,120]
peso = [10,20,30]
capacidad = 50
print(mochilla(capacidad,valor,peso))