"""
Se te da un arreglo arr[] que contiene las longitudes de n cuerdas. Queremos conectar todas las cuerdas en una sola cuerda.

📌 Regla del costo:

El costo de unir dos cuerdas es igual a la suma de sus longitudes.
Después de unirlas, la cuerda resultante puede volver a conectarse en los pasos siguientes.
🎯 Objetivo: Encontrar el costo mínimo total para conectar todas las cuerdas en una sola.

📥 Entrada
arr[]: arreglo de enteros positivos, longitudes de las cuerdas.
📤 Salida
Un entero que representa el costo mínimo total de conectar todas las cuerdas.
✅ Ejemplos
Ejemplo 1 arr = [4, 3, 2, 6] Salida: 29

Explicación paso a paso (estrategia óptima):

Conectar 2 + 3 = 5 → cuerdas = [4, 5, 6], costo = 5.
Conectar 4 + 5 = 9 → cuerdas = [9, 6], costo = 5 + 9 = 14.
Conectar 9 + 6 = 15 → cuerdas = [15], costo = 14 + 15 = 29.

"""

import heapq

def conectar_cuerdas(arr):

    heapq.heapify(arr)

    total_cost = 0

    while len(arr) > 1:

        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        cost = a + b
        total_cost += cost

        heapq.heappush(arr, cost)

    return total_cost

arr = [4,3,2,6]

print(conectar_cuerdas(arr))