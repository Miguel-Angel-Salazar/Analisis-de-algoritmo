#Obtener la mínima ganancia en vez de máxima
def cortar_cuerda(precios, n):

    memo = {}

    def dp(longitud):

        if longitud == 0:
            return 0

        if longitud in memo:
            return memo[longitud]

        peor = float("inf")

        for i in range(1, longitud + 1):

            ganancia = precios[i - 1] + dp(longitud - i)

            peor = min(peor, ganancia)

        memo[longitud] = peor

        return peor

    return dp(n)
