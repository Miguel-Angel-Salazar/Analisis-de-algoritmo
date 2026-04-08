"""
Enunciado

Dado un arreglo de enteros positivos, encuentra todos los subconjuntos de tamaño k cuya suma sea impar.

Ejemplo:
nums = [1, 2, 3, 4]
k = 2

Soluciones:

[1, 2]
[1, 4]
[2, 3]
[3, 4]
"""
def subconjuntos_impares(nums, k):
    resultado = []

    def backtrack(i, actual, suma):
        if len(actual) == k:
            if suma % 2 == 1:
                resultado.append(actual[:])
            return

        if i == len(nums):
            return

        if len(actual) + (len(nums) - i) < k:
            return

        actual.append(nums[i])
        backtrack(i + 1, actual, suma + nums[i])
        actual.pop()

        backtrack(i + 1, actual, suma)

    backtrack(0, [], 0)
    return resultado
# Ejemplo de uso
nums = [1, 2, 3, 4]
k = 2
print(subconjuntos_impares(nums, k))
# Salida:
# [[1, 2], [1, 4], [2, 3], [3, 4]]  
