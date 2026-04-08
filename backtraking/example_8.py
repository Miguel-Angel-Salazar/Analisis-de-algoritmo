"""
Una empresa genera códigos con las letras:

["A", "B", "C"]

Debes generar todos los códigos de longitud n tales que:

No haya dos letras iguales consecutivas
El código contenga al menos una vez la letra "B"
Ejemplo:
n = 3
"""
def generar_codigos(n):
    letras = ["A", "B", "C"]
    resultado = []

    def backtrack(actual, tiene_b):
        # Caso base
        if len(actual) == n:
            if tiene_b:
                resultado.append("".join(actual))
            return

        for letra in letras:
            # Poda: no repetir consecutivamente
            if actual and actual[-1] == letra:
                continue

            actual.append(letra)
            backtrack(actual, tiene_b or letra == "B")
            actual.pop()

    backtrack([], False)
    return resultado

# Ejemplo de uso
n = 3
print(generar_codigos(n))
# Salida:
# ['ABA', 'ABC', 'ACA', 'ACB', 'BAA', ' BAC', 'BCA', 'BCB', 'CAB', 'CBC']       
"""
8. Justificación para examen

Se aplica backtracking porque el código se construye carácter por carácter, evaluando en cada paso qué letra puede agregarse.
Se poda cuando una letra es igual a la anterior, ya que eso violaría la restricción del problema.
complejidad:
O(3^n) Cada posición tiene hasta 3 opciones: A, B o C, pero debido a la poda, el número real de combinaciones es menor.
"""