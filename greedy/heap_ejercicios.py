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

def solucion_asignar_tareas(tareas, num_servidores):
    if not tareas:
        return 0, [[] for _ in range(num_servidores)]
    
    # Ordenar tareas de mayor a menor (LPT - Longest Processing Time)
    tareas_ordenadas = sorted(enumerate(tareas), key=lambda x: -x[1])
    
    # Heap: (carga_actual, id_servidor, lista_tareas)
    servidores = [(0, i, []) for i in range(num_servidores)]
    heapq.heapify(servidores)
    
    for idx_original, tiempo in tareas_ordenadas:
        carga, id_servidor, lista = heapq.heappop(servidores)
        lista.append(tiempo)
        heapq.heappush(servidores, (carga + tiempo, id_servidor, lista))
    
    # Encontrar el tiempo máximo
    tiempo_total = max(s[0] for s in servidores)
    asignacion = [s[2] for s in sorted(servidores, key=lambda x: x[1])]
    
    return tiempo_total, asignacion

num_servidores = 3
tareas = [10, 30, 20,20,15]
print(solucion_asignar_tareas(tareas,num_servidores))