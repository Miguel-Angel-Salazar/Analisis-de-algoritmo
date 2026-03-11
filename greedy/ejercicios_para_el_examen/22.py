"""
Calificaciones:

[95,88,72,60,99,81,77]

Número de becas:

3

Solo estudiantes con nota ≥ 80.
"""
def becas(estudiantes, num_becas):

    elegibles = [e for e in estudiantes if e >= 80]
    elegibles.sort(reverse=True)

    return elegibles[:num_becas]


notas = [95,88,72,60,99,81,77]
print(becas(notas,3))
#Seleccionar siempre los estudiantes con mayor calificación.