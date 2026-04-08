"""
Enunciado

Dado un conjunto de empleados y turnos, y una disponibilidad por turno, genera todas las asignaciones válidas tales que:

Cada turno tenga exactamente un empleado
Ningún empleado trabaje en más de un turno
Ejemplo:
empleados = ["Ana", "Luis", "Carlos"]
turnos = ["Mañana", "Tarde"]

disponibilidad = {
    "Mañana": ["Ana", "Luis"],
    "Tarde": ["Luis", "Carlos"]
}
"""
def asignar_turnos(turnos, disponibilidad):
    resultado = []

    def backtrack(i, asignacion, usados):
        # Caso base
        if i == len(turnos):
            resultado.append(asignacion.copy())
            return

        turno = turnos[i]

        for empleado in disponibilidad[turno]:
            # Poda: no repetir empleado
            if empleado in usados:
                continue

            asignacion[turno] = empleado
            usados.add(empleado)

            backtrack(i + 1, asignacion, usados)

            usados.remove(empleado)
            del asignacion[turno]

    backtrack(0, {}, set())
    return resultado

turnos = ["Mañana", "Tarde"]
disponibilidad = {
    "Mañana": ["Ana", "Luis"],
    "Tarde": ["Luis", "Carlos"]
}

print(asignar_turnos(turnos, disponibilidad))
"""
O(m^n)
m = empleados posibles
n = cantidad de turnos
8. Justificación para examen

Se utiliza backtracking porque el problema consiste en construir una asignación válida turno por turno.
Se poda cuando un empleado ya ha sido asignado previamente, ya que no puede ocupar más de un turno.
"""