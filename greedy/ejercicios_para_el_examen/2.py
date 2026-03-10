"""
Tienes n actividades, cada una con un tiempo de inicio start[i] y un tiempo de fin finish[i]. Una persona solo puede realizar una actividad a la vez y puede iniciar una nueva actividad únicamente si su tiempo de inicio es estrictamente mayor o igual al tiempo de fin de la última actividad seleccionada.

🎯 Objetivo: Seleccionar el máximo número de actividades no solapadas.

📥 Entrada
Dos arreglos de tamaño n:

start[]: tiempos de inicio.
finish[]: tiempos de fin.
Se asume start[i] y finish[i] están emparejados por índice (i.e., describen la misma actividad).

📤 Salida
Un entero: máximo número de actividades que pueden realizarse sin solaparse.
(+1) La lista de índices de las actividades elegidas en orden de ejecución.
✅ Ejemplos
Ejemplo 1 start = [1, 3, 0, 5, 8, 5] finish = [2, 4, 6, 7, 9, 9] Salida: 4 Una selección posible (por índices): {0, 1, 3, 4}

Ejemplo 2 start = [10, 12, 20] finish = [20, 25, 30] Salida: 1
"""

def activity_selection(start, finish):

    actividades = list(zip(start, finish, range(len(start))))

    actividades.sort(key=lambda x: x[1])

    seleccion = [actividades[0][2]]

    last_finish = actividades[0][1]

    for s, f, idx in actividades[1:]:

        if s >= last_finish:
            seleccion.append(idx)
            last_finish = f

    return len(seleccion), seleccion


start = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]

print(activity_selection(start, finish))