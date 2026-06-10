"""
Máquina expendedora

Monedas:

1
3
4

Monto:

N

Encontrar el mínimo número de monedas.

Solución
Paradigma:
DP

Estado:
memo[monto]

Caso base:
monto == 0

Operación:
min
"""
monedas_disponibles = [1,3,4]

N = 6

memo = {}

def monedas(monto):

    if monto == 0:
        return 0

    if monto < 0:
        return float("inf")

    if monto in memo:
        return memo[monto]

    mejor = float("inf")

    for moneda in monedas_disponibles:

        mejor = min(
            mejor,
            1 + monedas(monto-moneda)
        )

    memo[monto] = mejor

    return memo[monto]

print(monedas(N))