#Algunas combinaciones de colores están prohibidas
def pintar_casas(costos, k):

    n = len(costos)

    prohibidos = {
        (2, 0)
    }

    memo = {}

    def dp(casa, color_anterior):

        if casa == n:
            return 0

        if (casa, color_anterior) in memo:
            return memo[(casa, color_anterior)]

        mejor = float("inf")

        for color in range(k):

            if (color_anterior, color) in prohibidos:
                continue

            if color != color_anterior:

                costo = (
                    costos[casa][color]
                    + dp(casa + 1, color)
                )

                mejor = min(mejor, costo)

        memo[(casa, color_anterior)] = mejor

        return mejor

    return dp(0, -1)
