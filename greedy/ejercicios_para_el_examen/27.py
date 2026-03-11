"""
Enunciado

Una carretera va de 0 a 20 km.

Tienes estaciones de servicio que cubren intervalos:

(0,5)
(3,9)
(6,12)
(10,15)
(14,20)
(8,18)

Objetivo:

usar el menor número de estaciones para cubrir toda la carretera
"""
def cubrir_carretera(intervalos, inicio, fin):

    # Idea Greedy:
    # Desde la posición actual elegimos el intervalo que empiece antes o igual
    # y que llegue lo más lejos posible. Esto minimiza el número de intervalos
    # necesarios para cubrir toda la carretera.

    intervalos.sort()
    i = 0
    n = len(intervalos)
    actual = inicio
    usados = []

    while actual < fin:
        mejor = actual

        while i < n and intervalos[i][0] <= actual:
            mejor = max(mejor, intervalos[i][1])
            i += 1

        if mejor == actual:
            return []

        usados.append(mejor)
        actual = mejor

    return usados


intervalos = [(0,5),(3,9),(6,12),(10,15),(14,20),(8,18)]
print(cubrir_carretera(intervalos,0,20))