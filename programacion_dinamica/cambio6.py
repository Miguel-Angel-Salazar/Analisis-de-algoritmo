#Retornar también los colores usados
def pintar_casas(costos, k):

    n = len(costos)

    memo = {}

    def dp(casa, color_anterior):

        if casa == n:
            return 0, []

        if (casa, color_anterior) in memo:
            return memo[(casa, color_anterior)]

        mejor = float("inf")
        mejores_colores = []

        for color in range(k):

            if color != color_anterior:

                costo_restante, colores_restantes = dp(
                    casa + 1,
                    color
                )

                costo_total = (
                    costos[casa][color]
                    + costo_restante
                )

                if costo_total < mejor:
                    mejor = costo_total
                    mejores_colores = [color] + colores_restantes

        memo[(casa, color_anterior)] = (
            mejor,
            mejores_colores
        )

        return memo[(casa, color_anterior)]

    return dp(0, -1)
