"""
Tienes actividades:

(inicio,fin)

Quieres asistir al máximo número.

Solución
Greedy

Ordenar por:
fin

Tomar:
la que termina primero

Complejidad:

O(n log n)
"""
intervalos = [
    (1,4),
    (3,5),
    (0,6),
    (5,7),
    (8,9)
]

intervalos.sort(
    key=lambda x:x[1]
)

cantidad = 0
ultimo_fin = -1

for inicio,fin in intervalos:

    if inicio >= ultimo_fin:

        cantidad += 1
        ultimo_fin = fin

print(cantidad)