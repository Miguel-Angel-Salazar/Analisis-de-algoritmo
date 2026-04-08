"""
EJERCICIO 3 — Cadenas binarias sin dos 1 seguidos
Enunciado

Genera todas las cadenas binarias de longitud n que no tengan dos 1 consecutivos.

Ejemplo:

Para n = 3:

000
001
010
100
101
"""
def binarias_sin_unos_consecutivos(n):
    resultado = []

    def backtrack(cadena):
        if len(cadena) == n:
            resultado.append("".join(cadena))
            return

        cadena.append("0")
        backtrack(cadena)
        cadena.pop()

        if not cadena or cadena[-1] != "1":
            cadena.append("1")
            backtrack(cadena)
            cadena.pop()

    backtrack([])
    return resultado

# ── Ejemplo 3: Cadenas binarias sin dos 1 seguidos ──
print("\n3. CADENAS BINARIAS SIN DOS 1 SEGUIDOS")
print("-" * 50)
n = 5
print(f"Cadenas binarias de longitud {n} sin dos 1 seguidos:")
print(binarias_sin_unos_consecutivos(n))

"""
Cómo justificar la poda

Se poda cuando la cadena parcial termina en 1 y se intenta agregar otro 1, ya que esto violaría la restricción del problema.

Muy limpia.
"""