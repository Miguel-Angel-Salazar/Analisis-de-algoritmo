import heapq

def asignar(tareas, servidores):

    heap = [(0, i) for i in range(servidores)]
    heapq.heapify(heap)

    for t in tareas:

        carga, id_servidor = heapq.heappop(heap)

        nueva_carga = carga + t

        heapq.heappush(heap, (nueva_carga, id_servidor))

    return heap