"""
Enunciado

Dada una lista de materias y una lista de pares incompatibles por cruce de horario, genera todas las selecciones de tamaño k tales que ninguna materia sea incompatible con otra.

Ejemplo:
materias = ["MAT", "FIS", "PROG", "BD", "REDES"]
incompatibles = {("MAT", "FIS"), ("PROG", "BD")}
k = 3
"""
def materias_compatibles(materias, incompatibles, k):
    resultado = []

    def es_compatible(actual, materia):
        for m in actual:
            if (m, materia) in incompatibles or (materia, m) in incompatibles:
                return False
        return True

    def backtrack(i, actual):
        # Caso base válido
        if len(actual) == k:
            resultado.append(actual[:])
            return

        # Si se acabaron las materias
        if i == len(materias):
            return

        # Poda: ya no alcanza
        if len(actual) + (len(materias) - i) < k:
            return

        # Opción 1: tomar materia si es compatible
        if es_compatible(actual, materias[i]):
            actual.append(materias[i])
            backtrack(i + 1, actual)
            actual.pop()

        # Opción 2: no tomarla
        backtrack(i + 1, actual)

    backtrack(0, [])
    return resultado

materias = ["MAT", "FIS", "PROG", "BD", "REDES"]
incompatibles = {("MAT", "FIS"), ("PROG", "BD")}

print(materias_compatibles(materias, incompatibles, 3))
"""
complejidad: O(2^n) en el peor caso, ya que cada materia puede ser tomada o no, pero la poda reduce significativamente 
el número de combinaciones a evaluar.
8. Justificación de poda

Se poda una rama cuando la materia actual es incompatible con alguna materia ya seleccionada, porque esa selección parcial no puede convertirse en una solución válida.
También se poda cuando ya no quedan suficientes materias para completar una selección de tamaño k.

💥 Muy buena explicación de parcial.
"""