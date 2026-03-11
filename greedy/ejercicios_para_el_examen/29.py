"""
Enunciado

Tienes tareas con duración:

[8, 5, 4, 3, 2, 1]

Hay 3 servidores.

Cada tarea debe ejecutarse completa en un solo servidor.

Objetivo:

minimizar el tiempo en que termina el último servidor
"""
import heapq

def asignar_tareas(tareas, servidores):

    # Idea Greedy:
    # Para minimizar el tiempo final, asignamos cada tarea al servidor
    # que esté menos ocupado en ese momento. Usamos un min-heap para
    # obtener rápidamente el servidor con menor carga.

    tareas.sort(reverse=True)

    heap = [(0,i) for i in range(servidores)]
    heapq.heapify(heap)

    for t in tareas:
        carga, id_servidor = heapq.heappop(heap)
        heapq.heappush(heap, (carga + t, id_servidor))

    return heap


print(asignar_tareas([8,5,4,3,2,1],3))