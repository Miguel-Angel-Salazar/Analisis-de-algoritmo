# Dado un arreglo de enteros, determinar si existen tres elementos distintos
# (por posición) cuya suma sea exactamente 0. Retornar True/False.
#
# Ejemplo:
#   entrada: [-1, 0, 1, 2, -1, -4]
#   salida: True (porque -1 + 0 + 1 = 0)


def solucion_tres_suman_cero(lista):
    for i in range(len(lista)):
        for j in range(i + 1,len(lista)):
            for k in range(j + 1,len(lista)):
                if lista[i] + lista[j] + lista[k] == 0:
                    return True
    return False


lista = [-1, 0, 1, 2, -1, -4]
resultado = solucion_tres_suman_cero(lista)
print(f"la salida es: {resultado}")