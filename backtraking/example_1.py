"""
Enunciado

Dado un arreglo de números positivos y un valor objetivo T, encuentra todas las combinaciones de números cuya suma sea exactamente T.
Cada número puede usarse a lo sumo una vez.

Ejemplo:
nums = [2, 3, 5, 6, 8]
T = 10

Soluciones:

[2, 3, 5]
[2, 8]
"""
def combinaciones_suma(nums, T):
    resultado = []

    def backtrack(i, actual, suma):
        if suma == T:
            resultado.append(actual[:])
            return

        if suma > T:
            return

        if i == len(nums):
            return

        # Tomar nums[i]
        actual.append(nums[i])
        backtrack(i + 1, actual, suma + nums[i])
        actual.pop()

        # No tomar nums[i]
        backtrack(i + 1, actual, suma)

    backtrack(0, [], 0)
    return resultado

# ── Ejemplo 1: Combinaciones de suma ──
print("1. COMBINACIONES DE SUMA")
print("-" * 50)
nums = [2, 3, 5, 6, 8]
T = 10
print("Números:", nums)
print("Objetivo:", T)
print("Combinaciones que suman T:", combinaciones_suma(nums, T))

"""
Cómo justificar la poda en examen

Se poda cuando la suma parcial supera el objetivo, ya que todos los números son positivos y seguir agregando solo aumentaría más la suma.

🔥 Esa justificación está perfecta.
"""