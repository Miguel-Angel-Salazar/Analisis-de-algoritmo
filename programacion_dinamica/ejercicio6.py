def minimo_saltos(arr, indice=0, memo=None):

    if memo is None:
        memo = {}

    if indice >= len(arr) - 1:
        return 0

    if arr[indice] == 0:
        return float("inf")

    if indice in memo:
        return memo[indice]

    minimo = float("inf")

    for salto in range(1, arr[indice] + 1):

        resultado = minimo_saltos(
            arr,
            indice + salto,
            memo
        )

        minimo = min(minimo, resultado + 1)

    memo[indice] = minimo

    return memo[indice]


# Complejidad: O(n²)
