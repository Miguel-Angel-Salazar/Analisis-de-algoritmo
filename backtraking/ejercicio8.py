def contar_caminos(matriz):
    filas, columnas = len(matriz), len(matriz[0])
    solucion = [[0]*columnas for _ in range(filas)]
    contador = 0

    def bt(fila, col):
        nonlocal contador

        if fila >= filas or col >= columnas or matriz[fila][col] != 0:
            return
        solucion[fila][col] = "*"
        if fila == filas - 1 and col == columnas - 1:
            contador += 1
        else:
            bt(fila, col + 1)
            bt(fila + 1, col)
        solucion[fila][col] = 0

    bt(0, 0)
    return contador


lab = [
    [0, 0, 1],
    [1, 0, 0],
    [1, 1, 0]
]

print(contar_caminos(lab))  