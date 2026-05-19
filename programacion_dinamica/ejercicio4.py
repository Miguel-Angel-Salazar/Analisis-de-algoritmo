def cortar_barra(precios, longitud, memo=None):

    if memo is None:
        memo = {}

    if longitud == 0:
        return 0

    if longitud in memo:
        return memo[longitud]

    maxima_ganancia = 0

    for tamaño_corte in range(1, longitud + 1):

        ganancia = precios[tamaño_corte - 1] + cortar_barra(
            precios,
            longitud - tamaño_corte,
            memo
        )

        maxima_ganancia = max(
            maxima_ganancia,
            ganancia
        )

    memo[longitud] = maxima_ganancia

    return memo[longitud]
