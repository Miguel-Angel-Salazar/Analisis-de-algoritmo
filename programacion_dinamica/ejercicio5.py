# ═══════════════════════════════════════════════════════════════════════════
# EJERCICIO 1: Camino mínimo en una cuadrícula
# ═══════════════════════════════════════════════════════════════════════════

def camino_minimo(matriz, fila=0, columna=0, memo=None):

    if memo is None:
        memo = {}

    filas = len(matriz)
    columnas = len(matriz[0])

    if fila >= filas or columna >= columnas:
        return float("inf")

    if fila == filas - 1 and columna == columnas - 1:
        return matriz[fila][columna]

    clave = (fila, columna)

    if clave in memo:
        return memo[clave]

    derecha = camino_minimo(
        matriz,
        fila,
        columna + 1,
        memo
    )

    abajo = camino_minimo(
        matriz,
        fila + 1,
        columna,
        memo
    )

    memo[clave] = matriz[fila][columna] + min(
        derecha,
        abajo
    )

    return memo[clave]


# Complejidad: O(filas * columnas)
