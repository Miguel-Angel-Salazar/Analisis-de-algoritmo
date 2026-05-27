#Maximizar costo en vez de minimizar
def pintar_casas(costos, k):

    n = len(costos)

    memo = {}

    def dp(casa, color_anterior):

        if casa == n:
            return 0

        if (casa, color_anterior) in memo:
            return memo[(casa, color_anterior)]

        peor = 0

        for color in range(k):

            if color != color_anterior:

                costo = (
                    costos[casa][color]
                    + dp(casa + 1, color)
                )

                peor = max(peor, costo)

        memo[(casa, color_anterior)] = peor

        return peor

    return dp(0, -1)
