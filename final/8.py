"""
Ejercicio estilo final #5 (Mochila disfrazada)
Selección de cursos

Tienes:

horas
beneficio

Dispones de:

40 horas

Cada curso puede tomarse una sola vez.

Maximizar beneficio.

Solución
Paradigma:
DP

Problema:
Mochila 0/1

Estado:
memo[(i,horas)]

Operación:
max
"""
pesos = [2,3,4,5]
valores = [3,4,5,8]

W = 5

memo = {}

def mochila(i,capacidad):

    if i == len(pesos):
        return 0

    if (i,capacidad) in memo:
        return memo[(i,capacidad)]

    if pesos[i] > capacidad:
        return mochila(i+1,capacidad)

    tomar = valores[i] + mochila(
        i+1,
        capacidad-pesos[i]
    )

    no_tomar = mochila(
        i+1,
        capacidad
    )

    memo[(i,capacidad)] = max(
        tomar,
        no_tomar
    )

    return memo[(i,capacidad)]

print(mochila(0,W))