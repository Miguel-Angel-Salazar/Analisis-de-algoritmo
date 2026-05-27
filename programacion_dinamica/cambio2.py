#Limitar cantidad máxima de cortes
def cortar_cuerda(precios, n, k):

    memo = {}

    def dp(longitud, cortes_restantes):

        if longitud == 0:
            return 0

        if cortes_restantes == 0:
            return float("-inf")

        if (longitud, cortes_restantes) in memo:
            return memo[(longitud, cortes_restantes)]

        mejor = 0

        for i in range(1, longitud + 1):

            ganancia = precios[i - 1] + dp(
                longitud - i,
                cortes_restantes - 1
            )

            mejor = max(mejor, ganancia)

        memo[(longitud, cortes_restantes)] = mejor

        return mejor

    return dp(n, k)
