"""
Enunciado

Dadas letras distintas, genera todas las palabras de longitud k sin repetir letras.

Ejemplo:
letras = ["A", "B", "C", "D"]
k = 3
"""

def palabras(letras, k):
    resultado = []
    usadas = [False] * len(letras)

    def backtrack(actual):
        if len(actual) == k:
            resultado.append("".join(actual))
            return

        for i in range(len(letras)):
            if not usadas[i]:
                usadas[i] = True
                actual.append(letras[i])

                backtrack(actual)

                actual.pop()
                usadas[i] = False

    backtrack([])
    return resultado

# ── Ejemplo 1: Generar palabras sin repetir letras ──
print("1. GENERAR PALABRAS SIN REPETIR LETRAS")         
print("-" * 50)
letras = ["A", "B", "C", "D"]
k = 3
print("Letras:", letras)
print("Palabras de longitud k sin repetir letras:", palabras(letras, k))

"""
Justificación de poda

Se evita explorar ramas donde una letra ya fue utilizada, porque el problema exige que no haya repeticiones.
"""
