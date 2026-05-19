def particion(nums):

    suma_total = sum(nums)

    if suma_total % 2 != 0:
        return False

    objetivo = suma_total // 2

    memo = {}

    def dp(indice, suma_actual):

        if suma_actual == objetivo:
            return True

        if indice >= len(nums) or suma_actual > objetivo:
            return False

        clave = (indice, suma_actual)

        if clave in memo:
            return memo[clave]

        tomar = dp(
            indice + 1,
            suma_actual + nums[indice]
        )

        no_tomar = dp(
            indice + 1,
            suma_actual
        )

        memo[clave] = tomar or no_tomar

        return memo[clave]

    return dp(0, 0)


# Complejidad: O(n * suma_total)
