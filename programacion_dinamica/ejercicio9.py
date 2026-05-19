def decodificaciones(cadena, indice=0, memo=None):

    if memo is None:
        memo = {}

    if indice == len(cadena):
        return 1

    if cadena[indice] == "0":
        return 0

    if indice in memo:
        return memo[indice]

    formas = decodificaciones(
        cadena,
        indice + 1,
        memo
    )

    if indice + 1 < len(cadena):

        numero = int(cadena[indice:indice + 2])

        if 10 <= numero <= 26:

            formas += decodificaciones(
                cadena,
                indice + 2,
                memo
            )

    memo[indice] = formas

    return memo[indice]


# Complejidad: O(n)
