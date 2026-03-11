"""
Enunciado

Tareas (tiempo, penalización):

(2,50)
(1,10)
(3,60)
(2,30)

Minimizar penalización total.
"""
def ordenar_tareas(tareas):

    tareas.sort(key=lambda x: x[1], reverse=True)

    return tareas


tareas = [(2,50),(1,10),(3,60),(2,30)]
print(ordenar_tareas(tareas))
#Ejecutar primero las tareas con mayor penalización.