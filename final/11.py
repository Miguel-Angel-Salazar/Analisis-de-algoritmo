"""
Mochila fraccionaria

Tienes objetos con:

peso
valor

Puedes partirlos.

Capacidad:

W
Solución
Greedy

valor/peso

Ordenar descendente
"""
objetos = [
    (10,60),
    (20,100),
    (30,120)
]

W = 50

objetos.sort(
    key=lambda x:x[1]/x[0],
    reverse=True
)

valor_total = 0

for peso,valor in objetos:

    if W >= peso:

        valor_total += valor
        W -= peso

    else:

        fraccion = W/peso

        valor_total += valor*fraccion

        break

print(valor_total)