"""
Desde el punto actual seleccionar el intervalo que empiece antes o igual
y que extienda la cobertura lo más lejos posible.
"""
def cubrir_carretera(intervalos, inicio, fin):

    intervalos.sort()  # ordenar por inicio
    i = 0
    n = len(intervalos)

    posicion = inicio
    seleccionados = []

    while posicion < fin:

        mejor_fin = posicion
        mejor_intervalo = None

        while i < n and intervalos[i][0] <= posicion:
            if intervalos[i][1] > mejor_fin:
                mejor_fin = intervalos[i][1]
                mejor_intervalo = intervalos[i]
            i += 1

        if mejor_intervalo is None:
            return None  # no se puede cubrir

        seleccionados.append(mejor_intervalo)
        posicion = mejor_fin

    return seleccionados


intervalos = [(0,5),(3,8),(6,10),(9,14),(13,18),(17,20),(4,12)]

print(cubrir_carretera(intervalos,0,20))