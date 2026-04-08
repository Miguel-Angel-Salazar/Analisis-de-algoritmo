"""
EJERCICIO 4 — Selección de tareas con tiempo límite
Enunciado

Tienes varias tareas, cada una con una duración.
Encuentra todas las formas de seleccionar tareas de modo que el tiempo total no supere un límite L.

Ejemplo:
tareas = [2, 4, 5, 3]
L = 7
"""
def seleccionar_tareas(tareas, L):
    resultado = []

    def backtrack(i, actual, tiempo):
        if tiempo > L:
            return

        if i == len(tareas):
            resultado.append(actual[:])
            return

        actual.append(tareas[i])
        backtrack(i + 1, actual, tiempo + tareas[i])
        actual.pop()

        backtrack(i + 1, actual, tiempo)

    backtrack(0, [], 0)
    return resultado

# ── Ejemplo 4: Selección de tareas con tiempo límite ──    
print("\n4. SELECCIÓN DE TAREAS CON TIEMPO LÍMITE")
print("-" * 50)
tareas = [2, 4, 5, 3]
L = 7
print("Tareas:", tareas)
print("Límite de tiempo:", L)
print("Combinaciones de tareas que no superan el límite:", seleccionar_tareas(tareas, L))

"""
Justificación de poda

Se poda cuando el tiempo acumulado supera el límite permitido, ya que agregar más tareas solo incrementaría el tiempo total.
"""