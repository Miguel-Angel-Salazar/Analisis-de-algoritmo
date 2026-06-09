def min_cost(A, inicio, fin):

    x1, y1 = inicio
    x2, y2 = fin

    # imposible llegar moviendo solo derecha/abajo
    if x1 > x2 or y1 > y2:
        return float('inf')

    filas = x2 - x1 + 1
    cols = y2 - y1 + 1

    dp = [[0] * cols for _ in range(filas)]

    dp[0][0] = A[x1][y1]

    for i in range(filas):
        for j in range(cols):

            if i == 0 and j == 0:
                continue

            arriba = dp[i-1][j] if i > 0 else float('inf')
            izquierda = dp[i][j-1] if j > 0 else float('inf')

            dp[i][j] = min(arriba, izquierda) + A[x1+i][y1+j]

    return dp[-1][-1]

def ruta_minima(A, p1, p2):

    n = len(A)
    m = len(A[0])

    fin = (n-1, m-1)

    costo1 = (
        min_cost(A, (0,0), p1)
        + min_cost(A, p1, p2)
        + min_cost(A, p2, fin)
        - A[p1[0]][p1[1]]
        - A[p2[0]][p2[1]]
    )

    costo2 = (
        min_cost(A, (0,0), p2)
        + min_cost(A, p2, p1)
        + min_cost(A, p1, fin)
        - A[p1[0]][p1[1]]
        - A[p2[0]][p2[1]]
    )

    respuesta = min(costo1, costo2)

    if respuesta == float('inf'):
        return -1

    return respuesta

A = [
    [1,3,1],
    [2,1,4],
    [3,2,1]
]

p1 = (1,0)
p2 = (1,1)

print(ruta_minima(A,p1,p2))