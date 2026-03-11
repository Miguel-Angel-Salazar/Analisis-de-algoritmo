"""
Enunciado

Tienes archivos con tamaños:

[5, 2, 4, 7, 1]

Para fusionar dos archivos el costo es la suma de sus tamaños.

Objetivo:

fusionar todos los archivos minimizando el costo total
"""
import heapq

def costo_minimo_fusion(archivos):

    # Idea Greedy:
    # Para minimizar el costo total de fusiones, siempre fusionamos primero
    # los dos archivos más pequeños. Usamos un min-heap para obtenerlos
    # rápidamente en cada paso.

    heapq.heapify(archivos)
    costo_total = 0

    while len(archivos) > 1:
        a = heapq.heappop(archivos)
        b = heapq.heappop(archivos)

        costo = a + b
        costo_total += costo

        heapq.heappush(archivos, costo)

    return costo_total


print(costo_minimo_fusion([5,2,4,7,1]))