"""
Cajas con volumen:

[4,8,1,4,2,1]

Capacidad de contenedor:

10

Objetivo:

usar el menor número de contenedores
"""
#Ordenar cajas y llenar cada contenedor con la combinación que más se acerque a la capacidad.
def empaquetar(cajas, capacidad):

    cajas.sort()
    i = 0
    j = len(cajas) - 1
    contenedores = []

    while i <= j:

        if cajas[i] + cajas[j] <= capacidad:
            contenedores.append((cajas[j], cajas[i]))
            i += 1
            j -= 1
        else:
            contenedores.append((cajas[j],))
            j -= 1

    return contenedores


cajas = [4,8,1,4,2,1]
print(empaquetar(cajas,10))