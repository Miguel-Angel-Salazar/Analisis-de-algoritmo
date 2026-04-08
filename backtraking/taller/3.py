import time
# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLO 3: N-Reinas
# ═══════════════════════════════════════════════════════════════════════════
#
# Problema: Colocar N reinas en un tablero N×N sin que se ataquen entre sí.
#           Las reinas atacan en fila, columna y diagonales.
#
# Sin poda: O(nⁿ) — probar cada columna en cada fila
# Con poda: O(n!) — la poda elimina muchas ramas
#

# --- FUERZA BRUTA: Probar TODAS las posiciones ---
from itertools import product

def n_reinas_fuerza_bruta(n):
    """
    Genera todas las combinaciones de columnas (nⁿ) y filtra las válidas.
    Extremadamente lento para n > 8.
    """
    resultado = []
    for posiciones in product(range(n), repeat=n):
        valida = True
        for i in range(n):
            for j in range(i + 1, n):
                # Misma columna o misma diagonal
                if posiciones[i] == posiciones[j] or \
                   abs(posiciones[i] - posiciones[j]) == abs(i - j):
                    valida = False
                    break
            if not valida:
                break
        if valida:
            resultado.append(list(posiciones))
    return resultado


# --- BACKTRACKING ---
def n_reinas(n):
    """
    Resuelve el problema de las N-Reinas con backtracking.

    tablero[i] = columna donde está la reina de la fila i.
    La poda verifica columnas y diagonales ANTES de colocar.
    """
    resultado = []

    def es_valida(tablero, fila, col):
        for f in range(fila):
            # Misma columna o misma diagonal
            if tablero[f] == col or \
               abs(tablero[f] - col) == abs(f - fila):
                return False
        return True

    def backtrack(tablero, fila):
        if fila == n:
            resultado.append(tablero[:])
            return

        for col in range(n):
            if es_valida(tablero, fila, col):   # poda
                tablero.append(col)              # colocar reina
                backtrack(tablero, fila + 1)     # siguiente fila
                tablero.pop()                    # quitar reina

    backtrack([], 0)
    return resultado


def imprimir_tablero(solucion):
    """Imprime un tablero de N-Reinas de forma visual."""
    n = len(solucion)
    for fila in range(n):
        linea = ""
        for col in range(n):
            linea += " Q" if solucion[fila] == col else " ."
        print(f"    {linea}")


    # ── Ejemplo 3: N-Reinas ──
    print("\n3. N-REINAS (N=6)")
    print("-" * 50)

    inicio = time.time()
    fb = n_reinas_fuerza_bruta(6)
    tiempo_fb = time.time() - inicio

    inicio = time.time()
    bt = n_reinas(6)
    tiempo_bt = time.time() - inicio

    print(f"   Fuerza bruta: {len(fb)} soluciones en {tiempo_fb:.4f}s")
    print(f"   Backtracking: {len(bt)} soluciones en {tiempo_bt:.4f}s")
    print(f"   Speedup: {tiempo_fb / tiempo_bt:.1f}x más rápido")
    print(f"\n   Primera solución (N=6):")
    imprimir_tablero(bt[0])