def resolver_laberinto_corto(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    solucion = [[0]*columnas for _ in range(filas)]

    def bt(fila, col):
        if fila >= filas or col >= columnas or matriz[fila][col] != 0:
            return False

        solucion[fila][col] = "*"
        if fila == filas - 1 and col == columnas - 1:
            return True

        if bt(fila, col + 1) or bt(fila + 1, col):
            return True

        solucion[fila][col] = 0 
        return False

    bt(0, 0)
    return solucion


lab = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 1, 0]
]

for fila in resolver_laberinto_corto(lab):
    print(fila)