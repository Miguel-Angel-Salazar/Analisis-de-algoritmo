def min_viajes(paquetes, capacidad):

    # Idea Greedy:
    # Para minimizar el número de viajes, ordenamos los paquetes y en cada viaje
    # combinamos el paquete más pesado con el más ligero posible que aún quepa
    # en el camión. Así aprovechamos al máximo la capacidad en cada viaje.

    paquetes.sort()
    i = 0
    j = len(paquetes) - 1
    viajes = 0

    while i <= j:
        if paquetes[i] + paquetes[j] <= capacidad:
            i += 1
        j -= 1
        viajes += 1

    return viajes


print(min_viajes([1,2,3,4,5],7))

"""
Tienes paquetes con pesos:

[1, 2, 3, 4, 5]

Un camión puede cargar máximo 7 unidades de peso por viaje.
Cada viaje puede llevar varios paquetes siempre que no supere esa capacidad.

Objetivo:

minimizar el número de viajes
"""