def max_anuncios(intervalos):

    # Idea Greedy:
    # Para transmitir el máximo número de anuncios sin superposición,
    # se ordenan los intervalos por tiempo de finalización y siempre se
    # selecciona el que termina primero y no se solapa con el anterior.

    intervalos.sort(key=lambda x: x[1])

    seleccionados = []
    ultimo_fin = -float('inf')

    for inicio, fin in intervalos:
        if inicio >= ultimo_fin:
            seleccionados.append((inicio, fin))
            ultimo_fin = fin

    return seleccionados


intervalos = [(1,4),(2,6),(4,7),(6,9),(8,10)]
print(max_anuncios(intervalos))

"""
Enunciado

Una empresa quiere poner anuncios en horarios de televisión.

Cada anuncio tiene:

(inicio, fin)

Horarios disponibles:

(1,4)
(2,6)
(4,7)
(6,9)
(8,10)

No se pueden superponer anuncios.

Objetivo:

maximizar la cantidad de anuncios transmitidos
"""