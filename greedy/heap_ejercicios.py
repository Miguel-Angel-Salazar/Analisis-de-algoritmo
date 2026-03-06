import heapq

def asignar_tareas(tareas, num_servidores):
    tareas_ordenadas = sorted(enumerate(tareas), key=lambda x: x[1])
    servidores = [(0, i, []) for i in range(num_servidores)]
    heapq.heapify(servidores)

    for id_tarea, tiempo in tareas_ordenadas:
        carga, id_servidor, lista = heapq.heappop(servidores)
        lista.append(tiempo)
        heapq.heappush(servidores, (carga + tiempo, id_servidor, lista))

    return servidores

num_servidores = 3
tareas = [10, 30, 20,20,15]

resultado = asignar_tareas(tareas, num_servidores)
print(resultado)