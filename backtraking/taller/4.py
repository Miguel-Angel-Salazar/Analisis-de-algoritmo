import time
# ═══════════════════════════════════════════════════════════════════════════
# EJEMPLO 4: Suma de Subconjuntos
# ═══════════════════════════════════════════════════════════════════════════
#
# Problema: Encontrar todos los subconjuntos que sumen un valor objetivo.
# Ejemplo: nums=[2,3,5,8], objetivo=8 → [[3,5], [8]]
#
# Sin poda: O(2ⁿ)
# Con poda: mucho menor si ordenamos y cortamos cuando la suma se pasa
#

# --- FUERZA BRUTA: Generar todos los subconjuntos y filtrar ---
def suma_subconjuntos_fuerza_bruta(nums, objetivo):
    """Genera todos los 2ⁿ subconjuntos y filtra los que suman el objetivo."""
    n = len(nums)
    resultado = []
    for mascara in range(2 ** n):
        subconjunto = []
        for i in range(n):
            if mascara & (1 << i):
                subconjunto.append(nums[i])
        if sum(subconjunto) == objetivo:
            resultado.append(subconjunto)
    return resultado


# --- BACKTRACKING con poda ---
def suma_subconjuntos(nums, objetivo):
    """
    Encuentra subconjuntos que sumen el objetivo usando backtracking.

    Poda clave: si ordenamos los números, podemos hacer break
    cuando la suma parcial ya excede el objetivo.
    """
    resultado = []
    nums.sort()  # ordenar para habilitar la poda

    def backtrack(inicio, actual, suma):
        if suma == objetivo:
            resultado.append(actual[:])
            return

        for i in range(inicio, len(nums)):
            if suma + nums[i] > objetivo:   # poda: ya nos pasamos
                break
            actual.append(nums[i])           # elegir
            backtrack(i + 1, actual, suma + nums[i])  # explorar
            actual.pop()                     # deshacer

    backtrack(0, [], 0)
    return resultado

# ── Ejemplo 4: Suma de subconjuntos ──
print("\n4. SUMA DE SUBCONJUNTOS")
print("-" * 50)
nums = [2, 3, 5, 7, 8, 10]
objetivo = 15

inicio = time.time()
fb = suma_subconjuntos_fuerza_bruta(nums, objetivo)
tiempo_fb = time.time() - inicio

inicio = time.time()
bt = suma_subconjuntos(nums[:], objetivo)  # copia porque sort modifica
tiempo_bt = time.time() - inicio

print(f"   nums={nums}, objetivo={objetivo}")
print(f"   Fuerza bruta: {fb} - {tiempo_fb:.6f}s")
print(f"   Backtracking: {bt} - {tiempo_bt:.6f}s")