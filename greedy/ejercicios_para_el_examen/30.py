"""
Tienes objetos con:

(peso, valor)

(4,20)
(2,14)
(6,30)
(3,18)

Capacidad de la mochila:

10

Se permite tomar fracciones de objetos.

Objetivo:

maximizar el valor total
"""
def mochila_fraccionaria(capacidad, objetos):

    # Idea Greedy:
    # Para maximizar el valor en la mochila, seleccionamos primero los
    # objetos con mayor relación valor/peso. Si un objeto no cabe completo,
    # tomamos solo la fracción necesaria.

    objetos.sort(key=lambda x: x[1]/x[0], reverse=True)

    valor_total = 0

    for peso, valor in objetos:
        if capacidad >= peso:
            capacidad -= peso
            valor_total += valor
        else:
            valor_total += valor * (capacidad/peso)
            break

    return valor_total


objetos = [(4,20),(2,14),(6,30),(3,18)]
print(mochila_fraccionaria(10, objetos))