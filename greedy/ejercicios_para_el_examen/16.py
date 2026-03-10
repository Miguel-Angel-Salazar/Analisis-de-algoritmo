"""
Una universidad quiere apagar el mayor número posible de computadoras para ahorrar energía.
"""

def max_tareas(tareas):

    tareas = sorted(tareas, key=lambda x: x[2])

    tiempo = 0
    resultado = []

    for nombre, duracion, deadline in tareas:

        if tiempo + duracion <= deadline:
            tiempo += duracion
            resultado.append(nombre)

    return resultado

tareas = [
    ("A", 2, 4),   # nombre, tiempo_apagado, deadline
    ("B", 1, 3),
    ("C", 3, 5),
    ("D", 2, 6)
]
print(max_tareas(tareas))