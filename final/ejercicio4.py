"""
Recolección de energía

Una matriz contiene cantidades positivas de energía.

Empiezas en (0,0) y debes llegar a (n-1,m-1).

Solo puedes moverte:

↓
→

Algunas celdas contienen -1 y están bloqueadas.

Se desea obtener la máxima energía posible.
Paradigma:
DP

Estado:
memo[(i,j)]

Caso base:
if destino:
    return matriz[i][j]

Bloqueada:
return -inf

Operación:
max

Recurrencia:
actual + max(abajo,derecha)
"""
matriz = [
    [5, 2, 3],
    [1, -1, 4],
    [2, 8, 1]
]

n = len(matriz)
m = len(matriz[0])

memo = {}

def energia(i,j):

    if i >= n or j >= m:
        return float("-inf")

    if matriz[i][j] == -1:
        return float("-inf")

    if i == n-1 and j == m-1:
        return matriz[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    abajo = energia(i+1,j)
    derecha = energia(i,j+1)

    memo[(i,j)] = matriz[i][j] + max(abajo,derecha)

    return memo[(i,j)]

print(energia(0,0))