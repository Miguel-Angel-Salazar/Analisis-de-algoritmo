def contar_caminos(filas, columnas, fila=0, columna=0, memo=None):

    if memo is None:
        memo = {}

    if fila >= filas or columna >= columnas:
        return 0

    if fila == filas - 1 and columna == columnas - 1:
        return 1

    clave = (fila, columna)

    if clave in memo:
        return memo[clave]

    derecha = contar_caminos(
        filas,
        columnas,
        fila,
        columna + 1,
        memo
    )

    abajo = contar_caminos(
        filas,
        columnas,
        fila + 1,
        columna,
        memo
    )

    memo[clave] = derecha + abajo

    return memo[clave]


# Complejidad: O(filas * columnas)
