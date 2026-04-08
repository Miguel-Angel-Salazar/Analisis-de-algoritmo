# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLO 1: Generar Subconjuntos
# ═══════════════════════════════════════════════════════════════════════════
#
# Problema: Dado un conjunto de números, generar todos los subconjuntos.
# Ejemplo: [1, 2, 3] → [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
#
# Complejidad: O(2ⁿ × n) — hay 2ⁿ subconjuntos, copiar cada uno toma O(n)
#

# --- FUERZA BRUTA: Usar bits para generar todas las combinaciones ---
def subconjuntos_fuerza_bruta(nums):
    """
    Genera subconjuntos usando máscara de bits.
    Para cada número del 0 al 2ⁿ-1, los bits indican qué elementos incluir.
    """
    n = len(nums)
    resultado = []
    for mascara in range(2 ** n):
        subconjunto = []
        for i in range(n):
            if mascara & (1 << i):
                subconjunto.append(nums[i])
        resultado.append(subconjunto)
    return resultado


# --- BACKTRACKING ---
def subconjuntos(nums):
    """
    Genera todos los subconjuntos usando backtracking.

    El parámetro 'inicio' evita generar duplicados como [1,2] y [2,1].
    Cada nodo del árbol de recursión es un subconjunto válido.
    """
    resultado = []

    def backtrack(inicio, actual):
        resultado.append(actual[:])  # guardar copia del estado actual

        for i in range(inicio, len(nums)):
            actual.append(nums[i])      # elegir
            backtrack(i + 1, actual)     # explorar
            actual.pop()                 # deshacer

    backtrack(0, [])
    return resultado

if __name__ == "__main__":
    import time

    print("=" * 70)
    print("COMPARACIÓN: FUERZA BRUTA vs BACKTRACKING")
    print("=" * 70)

    # ── Ejemplo 1: Subconjuntos ──
    print("\n1. SUBCONJUNTOS de [1, 2, 3]")
    print("-" * 50)

    inicio = time.time()
    fb = subconjuntos_fuerza_bruta([1, 2, 3])
    tiempo_fb = time.time() - inicio

    inicio = time.time()
    bt = subconjuntos([1, 2, 3])
    tiempo_bt = time.time() - inicio

    print(f"   Fuerza bruta ({len(fb)} subconj.): {tiempo_fb:.6f}s")
    print(f"   Backtracking ({len(bt)} subconj.): {tiempo_bt:.6f}s")
    print(f"   Resultado: {bt}")
