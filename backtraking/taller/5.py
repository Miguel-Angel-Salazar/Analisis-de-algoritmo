import time
# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLO 5: Resolver Sudoku
# ═══════════════════════════════════════════════════════════════════════════
#
# Problema: Llenar un tablero 9×9 con números 1-9 siguiendo las reglas:
#           - No repetir en fila, columna ni caja 3×3
#
# Sin poda: O(9⁸¹) — probar 9 opciones en 81 celdas
# Con poda: mucho menor, solo probar números válidos
#

def resolver_sudoku(tablero):
    """
    Resuelve un Sudoku usando backtracking.
    Las celdas vacías se representan con 0.
    Modifica el tablero in-place y retorna True si tiene solución.
    """

    def encontrar_vacia(tablero):
        for i in range(9):
            for j in range(9):
                if tablero[i][j] == 0:
                    return (i, j)
        return None

    def es_valido(tablero, fila, col, num):
        # Verificar fila
        if num in tablero[fila]:
            return False

        # Verificar columna
        for i in range(9):
            if tablero[i][col] == num:
                return False

        # Verificar caja 3×3
        box_fila = (fila // 3) * 3
        box_col = (col // 3) * 3
        for i in range(box_fila, box_fila + 3):
            for j in range(box_col, box_col + 3):
                if tablero[i][j] == num:
                    return False

        return True

    vacia = encontrar_vacia(tablero)
    if not vacia:
        return True  # no hay celdas vacías → resuelto

    fila, col = vacia

    for num in range(1, 10):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num          # elegir

            if resolver_sudoku(tablero):      # explorar
                return True

            tablero[fila][col] = 0            # deshacer

    return False  # ningún número funcionó → backtrack


def imprimir_sudoku(tablero):
    """Imprime un tablero de Sudoku formateado."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("    ------+-------+------")
        fila = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                fila += " | "
            fila += f" {tablero[i][j]}" if tablero[i][j] != 0 else " ."
        print(f"    {fila}")


    # ── Ejemplo 5: Sudoku ──
    print("\n5. SUDOKU")
    print("-" * 50)

    tablero = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("   Tablero inicial:")
    imprimir_sudoku(tablero)

    inicio = time.time()
    resuelto = resolver_sudoku(tablero)
    tiempo = time.time() - inicio

    print(f"\n   Resuelto: {resuelto} en {tiempo:.4f}s")
    if resuelto:
        print("   Solución:")
        imprimir_sudoku(tablero)