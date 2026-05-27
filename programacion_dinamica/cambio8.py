#No se pueden repetir colores en distancia 2
def pintar_casas(costos, k):

    n = len(costos)

    memo = {}

    def dp(casa, color1, color2):

        if casa == n:
            return 0

        if (casa, color1, color2) in memo:
            return memo[(casa, color1, color2)]

        mejor = float("inf")

        for color in range(k):

            if color != color1 and color != color2:

                costo = (
                    costos[casa][color]
                    + dp(casa + 1, color2, color)
                )

                mejor = min(mejor, costo)

        memo[(casa, color1, color2)] = mejor

        return mejor

    return dp(0, -1, -1)
