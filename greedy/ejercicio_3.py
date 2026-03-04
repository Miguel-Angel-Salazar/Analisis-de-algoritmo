import heapq
actividades = [(1,4), (3,5),(0,6),(5,7),(6,10),(8,11)]

actividades_orden=sorted(actividades, key = lambda x: x[1])

teatro = []
orden = 0
for hora_inicio, hora_fin in actividades_orden:
    if hora_inicio >= orden:
        teatro.append((hora_inicio, hora_fin))
        orden = hora_fin
print("Mejor combinación:", teatro)
print("Cantidad máxima:", len(teatro))




