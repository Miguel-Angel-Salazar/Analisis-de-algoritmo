#Retornar también los cortes usados
def cortar_cuerda(precios, n):

    memo = {}

    def dp(longitud):

        if longitud == 0:
            return 0, []

        if longitud in memo:
            return memo[longitud]

        mejor_ganancia = 0
        mejores_cortes = []

        for i in range(1, longitud + 1):

            ganancia_restante, cortes_restantes = dp(longitud - i)

            ganancia_total = precios[i - 1] + ganancia_restante

            if ganancia_total > mejor_ganancia:
                mejor_ganancia = ganancia_total
                mejores_cortes = [i] + cortes_restantes

        memo[longitud] = (mejor_ganancia, mejores_cortes)

        return memo[longitud]

    return dp(n)
