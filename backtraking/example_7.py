"""
EJERCICIO 1 — Equipos de tamaño k con puntaje exacto
⭐ MUY TIPO EXAMEN
Enunciado

Tienes una lista de jugadores con puntajes.
Debes formar todos los equipos de tamaño k cuya suma de puntajes sea exactamente T.

Ejemplo:
jugadores = [("Ana", 3), ("Luis", 5), ("Carlos", 2), ("Marta", 4)]
k = 2
T = 7
Salida esperada:
[["Ana", "Marta"], ["Luis", "Carlos"]]
1. ¿Por qué esto es backtracking?

Porque:

estás eligiendo jugadores
construyes el equipo paso a paso
cada jugador se toma o no se toma
si ya te pasaste del puntaje o ya no puedes completar el equipo, podas

👉 Este es el modelo clásico de subconjuntos / combinaciones.
"""
def equipos_puntaje(jugadores, k, T):
    resultado = []

    def backtrack(i, equipo, suma_actual):
        # Caso base: si ya tengo k jugadores
        if len(equipo) == k:
            if suma_actual == T:
                resultado.append(equipo[:])
            return

        # Si ya recorrí todos los jugadores
        if i == len(jugadores):
            return

        # Poda 1: si la suma ya se pasó
        if suma_actual > T:
            return

        # Poda 2: si ya no alcanza para completar k
        if len(equipo) + (len(jugadores) - i) < k:
            return

        nombre, puntaje = jugadores[i]

        # Opción 1: tomar al jugador actual
        equipo.append(nombre)
        backtrack(i + 1, equipo, suma_actual + puntaje)
        equipo.pop()

        # Opción 2: no tomar al jugador actual
        backtrack(i + 1, equipo, suma_actual)

    backtrack(0, [], 0)
    return resultado
# Ejemplo de uso
jugadores = [("Ana", 3), ("Luis", 5), ("Carlos", 2), ("Marta", 4)]
k = 2
T = 7
print(equipos_puntaje(jugadores, k, T))
# Salida esperada:          
# [["Ana", "Marta"], ["Luis", "Carlos"]]

"""
Se utiliza backtracking porque el problema consiste en construir equipos válidos de manera incremental,
explorando las decisiones de incluir o no incluir cada jugador.
Se poda una rama cuando la suma parcial supera el objetivo o cuando
ya no quedan suficientes jugadores para completar un equipo de tamaño k
.
complejidad:    O(2^n) 
Porque para cada jugador decides:
tomarlo
no tomarlo
"""