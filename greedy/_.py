import heapq
actividades_1=[(4,1), (5,3),(6,0),(7,5),(10,6),(11,8)]

teatro_1 = []
for hora_final, hora_inicial in actividades_1:
    heapq.heappush(teatro_1,(hora_final,hora_inicial))

seleccionadas = []
hora_actual = 0

while teatro_1:
    hora_final, hora_inicial = heapq.heappop(teatro_1)

    if hora_inicial >= hora_actual:
        seleccionadas.append((hora_final, hora_inicial))
        hora_actual = hora_final

print(seleccionadas)
print(len(seleccionadas))