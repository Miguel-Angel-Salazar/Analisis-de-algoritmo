"""
EJERCICIO 2 — Formar grupos sin incompatibilidades
Enunciado

Tienes una lista de personas y una lista de pares incompatibles.
Debes formar un grupo de tamaño k sin incluir personas incompatibles entre sí.

Ejemplo:
personas = ["Ana", "Luis", "Carlos", "Sofia", "Marta"]
incompatibles = {("Ana", "Luis"), ("Carlos", "Sofia")}
k = 3
"""
def formar_grupos(personas, incompatibles, k):
    resultado = []

    def son_compatibles(grupo, persona):
        for p in grupo:
            if (p, persona) in incompatibles or (persona, p) in incompatibles:
                return False
        return True

    def backtrack(i, grupo):
        if len(grupo) == k:
            resultado.append(grupo[:])
            return

        if i == len(personas):
            return

        if len(grupo) + (len(personas) - i) < k:
            return

        if son_compatibles(grupo, personas[i]):
            grupo.append(personas[i])
            backtrack(i + 1, grupo)
            grupo.pop()

        backtrack(i + 1, grupo)

    backtrack(0, [])
    return resultado

# ── Ejemplo 2: Formar grupos sin incompatibilidades ──
print("\n2. FORMAR GRUPOS SIN INCOMPATIBILIDADES")                      
print("-" * 50)
personas = ["Ana", "Luis", "Carlos", "Sofia", "Marta"]
incompatibles = {("Ana", "Luis"), ("Carlos", "Sofia")}
k = 3
print("Personas:", personas)
print("Incompatibles:", incompatibles)
print("Grupos de tamaño k sin incompatibilidades:", formar_grupos(personas, incompatibles, k))

"""
Cómo justificar la poda

Se poda cuando el grupo parcial contiene una incompatibilidad, porque ya no puede convertirse en una solución válida.
También se poda cuando no quedan suficientes personas para completar el tamaño requerido del grupo.

💥 Esto es exactamente lo que suele preguntar un profe.
"""