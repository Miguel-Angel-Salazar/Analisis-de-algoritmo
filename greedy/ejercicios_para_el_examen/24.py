"""
Edificios en posiciones:

[2,4,7,10,13,15]

Un router cubre:

±2 metros

Objetivo:

poner el menor número de routers
"""

def colocar_wifi(edificios, rango):

    edificios.sort()
    i = 0
    n = len(edificios)
    routers = []

    while i < n:

        start = edificios[i]

        while i < n and edificios[i] <= start + rango:
            i += 1

        router = edificios[i-1]
        routers.append(router)

        while i < n and edificios[i] <= router + rango:
            i += 1

    return routers


edificios = [2,4,7,10,13,15]
print(colocar_wifi(edificios,2))

#Desde el edificio más a la izquierda colocar el router lo más a la derecha posible.