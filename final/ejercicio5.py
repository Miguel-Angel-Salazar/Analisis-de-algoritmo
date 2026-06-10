"""
Peaje mínimo

Una ciudad está representada por una matriz.

Cada celda tiene un costo.

Se quiere llegar desde (0,0) hasta (n−1,m−1).

Solo:

↓
→

Algunas calles están cerradas.

Determinar el costo mínimo.
Paradigma:
DP

Estado:
memo[(i,j)]

Caso base:
return matriz[i][j]

Bloqueada:
+inf

Operación:
min

Recurrencia:
actual + min(abajo,derecha)
"""
matriz = [
    [1,3,2],
    [2,5,1],
    [4,2,1]
]

n = len(matriz)
m = len(matriz[0])

memo = {}

def costo(i,j):

    if i >= n or j >= m:
        return float("inf")

    if i == n-1 and j == m-1:
        return matriz[i][j]

    if (i,j) in memo:
        return memo[(i,j)]

    abajo = costo(i+1,j)
    derecha = costo(i,j+1)

    memo[(i,j)] = matriz[i][j] + min(abajo,derecha)

    return memo[(i,j)]

print(costo(0,0))