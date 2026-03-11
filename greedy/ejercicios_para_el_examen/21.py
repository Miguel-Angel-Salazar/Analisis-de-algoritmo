"""
Barcos con peso:

[2,3,5,7,4,6]

Capacidad máxima por transporte:

10

Minimizar número de transportes.
"""
def cargar_barcos(pesos, capacidad):

    pesos.sort()
    i = 0
    j = len(pesos) - 1
    transportes = []

    while i <= j:

        if pesos[i] + pesos[j] <= capacidad:
            transportes.append((pesos[j], pesos[i]))
            i += 1
            j -= 1
        else:
            transportes.append((pesos[j],))
            j -= 1

    return transportes


pesos = [2,3,5,7,4,6]
print(cargar_barcos(pesos,10))

#Ordenar pesos y combinar el más pesado con el más ligero posible.