def ruta_minima(A, p1, p2):

    n = len(A)
    m = len(A[0])

    memo = {}

    def dp(i, j, xf, yf):

        if i > xf or j > yf:
            return float("inf")

        if i == xf and j == yf:
            return A[i][j]

        if (i,j,xf,yf) in memo:
            return memo[(i,j,xf,yf)]

        abajo = dp(i+1, j, xf, yf)
        derecha = dp(i, j+1, xf, yf)

        memo[(i,j,xf,yf)] = A[i][j] + min(abajo, derecha)

        return memo[(i,j,xf,yf)]

    r1 = (
        dp(0,0,p1[0],p1[1]) +
        dp(p1[0],p1[1],p2[0],p2[1]) +
        dp(p2[0],p2[1],n-1,m-1)
        - A[p1[0]][p1[1]]
        - A[p2[0]][p2[1]]
    )

    r2 = (
        dp(0,0,p2[0],p2[1]) +
        dp(p2[0],p2[1],p1[0],p1[1]) +
        dp(p1[0],p1[1],n-1,m-1)
        - A[p1[0]][p1[1]]
        - A[p2[0]][p2[1]]
    )

    ans = min(r1, r2)

    return -1 if ans == float("inf") else ans

A = [
    [1,3,1],
    [2,1,4],
    [3,2,1]
]

p1 = (1,0)
p2 = (1,1)

print(ruta_minima(A,p1,p2))