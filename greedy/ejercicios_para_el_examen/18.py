import math

def radares(islas, d):

    intervalos = []

    for x,y in islas:

        if y > d:
            return -1

        dx = math.sqrt(d**2 - y**2)

        intervalos.append((x-dx, x+dx))

    intervalos.sort(key=lambda x: x[1])

    radares = []
    pos = -float("inf")

    for inicio, fin in intervalos:

        if inicio > pos:
            pos = fin
            radares.append(pos)

    return radares

islas = [(1,2),(2,4),(5,3),(7,2),(9,1)]
print(radares(islas,5))

#Colocar cada radar lo más a la derecha posible sin perder la cobertura de la isla más restrictiva.