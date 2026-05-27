#Penalización por cada corte
def cortar_cuerda(precios, n):

    memo = {}

    def dp(longitud):

        if longitud == 0:
            return 0

        if longitud in memo:
            return memo[longitud]

        mejor = 0

        for i in range(1, longitud + 1):

            penalizacion = 0

            if i != longitud:
                penalizacion = 2

            ganancia = (
                precios[i - 1]
                + dp(longitud - i)
                - penalizacion
            )

            mejor = max(mejor, ganancia)

        memo[longitud] = mejor

        return mejor

    return dp(n)
