import time
# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLO 2: Permutaciones
# ═══════════════════════════════════════════════════════════════════════════
#
# Problema: Dado un conjunto de números, generar todas las permutaciones.
# Ejemplo: [1, 2, 3] → [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
#
# Complejidad: O(n! × n) — hay n! permutaciones, copiar cada una toma O(n)
#

# --- FUERZA BRUTA: Usar itertools ---
from itertools import permutations as itertools_permutations

def permutaciones_fuerza_bruta(nums):
    """Genera permutaciones usando itertools (referencia)."""
    return [list(p) for p in itertools_permutations(nums)]


# --- BACKTRACKING ---
def permutaciones(nums):
    """
    Genera todas las permutaciones usando backtracking.

    Diferencia con subconjuntos:
    - Subconjuntos: el orden NO importa → usar 'inicio' para avanzar
    - Permutaciones: el orden SÍ importa → verificar 'not in actual'
    """
    resultado = []

    def backtrack(actual):
        if len(actual) == len(nums):
            resultado.append(actual[:])
            return

        for num in nums:
            if num not in actual:        # poda: no repetir elementos
                actual.append(num)        # elegir
                backtrack(actual)         # explorar
                actual.pop()              # deshacer

    backtrack([])
    return resultado
# ── Ejemplo 2: Permutaciones ──
print("\n2. PERMUTACIONES de [1, 2, 3]")
print("-" * 50)

inicio = time.time()
fb = permutaciones_fuerza_bruta([1, 2, 3])
tiempo_fb = time.time() - inicio

inicio = time.time()
bt = permutaciones([1, 2, 3])
tiempo_bt = time.time() - inicio

print(f"   Fuerza bruta ({len(fb)} perm.): {tiempo_fb:.6f}s")
print(f"   Backtracking ({len(bt)} perm.): {tiempo_bt:.6f}s")
print(f"   Resultado: {bt}")