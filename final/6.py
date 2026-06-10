"""
Ruta turística

Una matriz representa costos.

Debes pasar obligatoriamente por:

A = (x1,y1)

B = (x2,y2)

Solo:

↓
→

Determinar el costo mínimo.
DP

inicio -> A -> B -> fin

inicio -> B -> A -> fin

Tomar el mínimo
"""
matriz = [
    [1,3,1],
    [2,1,4],
    [3,2,1]
]

n = len(matriz)
m = len(matriz[0])

p1 = (1,0)
p2 = (1,1)

memo = {}

def dp(i,j,xf,yf):

    if i > xf or j > yf:
        return float("inf")

    if i == xf and j == yf:
        return matriz[i][j]

    if (i,j,xf,yf) in memo:
        return memo[(i,j,xf,yf)]

    abajo = dp(i+1,j,xf,yf)
    derecha = dp(i,j+1,xf,yf)

    memo[(i,j,xf,yf)] = matriz[i][j] + min(abajo,derecha)

    return memo[(i,j,xf,yf)]

r1 = (
    dp(0,0,p1[0],p1[1]) +
    dp(p1[0],p1[1],p2[0],p2[1]) +
    dp(p2[0],p2[1],n-1,m-1)
    - matriz[p1[0]][p1[1]]
    - matriz[p2[0]][p2[1]]
)

r2 = (
    dp(0,0,p2[0],p2[1]) +
    dp(p2[0],p2[1],p1[0],p1[1]) +
    dp(p1[0],p1[1],n-1,m-1)
    - matriz[p1[0]][p1[1]]
    - matriz[p2[0]][p2[1]]
)

print(min(r1,r2))