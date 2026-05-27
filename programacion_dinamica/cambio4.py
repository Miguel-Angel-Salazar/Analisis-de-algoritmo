#Prohibir ciertos tamaños de corte
def cortar_cuerda(precios, n):

    memo = {}

    def dp(longitud):

        if longitud == 0:
            return 0

        if longitud in memo:
            return memo[longitud]

        mejor = 0

        for i in range(1, longitud + 1):

            if i == 3:
                continue

            ganancia = precios[i - 1] + dp(longitud - i)

            mejor = max(mejor, ganancia)

        memo[longitud] = mejor

        return mejor

    return mejor

    return dp(n)
