#Algunas casas ya tienen color fijo
def pintar_casas(costos, k, colores_fijos):

    n = len(costos)

    memo = {}

    def dp(casa, color_anterior):

        if casa == n:
            return 0

        if (casa, color_anterior) in memo:
            return memo[(casa, color_anterior)]

        mejor = float("inf")

        colores_posibles = range(k)

        if casa in colores_fijos:
            colores_posibles = [colores_fijos[casa]]

        for color in colores_posibles:

            if color != color_anterior:

                costo = (
                    costos[casa][color]
                    + dp(casa + 1, color)
                )

                mejor = min(mejor, costo)

        memo[(casa, color_anterior)] = mejor

        return mejor

    return dp(0, -1)
