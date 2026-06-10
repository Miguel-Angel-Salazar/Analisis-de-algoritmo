"""
Número de rutas

Una matriz tiene obstáculos.

Determinar cuántos caminos existen desde el inicio hasta el final.

Solo:

↓
→
Solución
Paradigma:
DP

Estado:
memo[(i,j)]

Caso base:
return 1

Bloqueada:
return 0

Operación:
suma

Recurrencia:
abajo + derecha
"""
matriz = [
    [0,0,0],
    [0,-1,0],
    [0,0,0]
]

n = len(matriz)
m = len(matriz[0])

memo = {}

def caminos(i,j):

    if i >= n or j >= m:
        return 0

    if matriz[i][j] == -1:
        return 0

    if i == n-1 and j == m-1:
        return 1

    if (i,j) in memo:
        return memo[(i,j)]

    abajo = caminos(i+1,j)
    derecha = caminos(i,j+1)

    memo[(i,j)] = abajo + derecha

    return memo[(i,j)]

print(caminos(0,0))