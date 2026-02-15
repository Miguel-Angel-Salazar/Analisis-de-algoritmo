# Dado un arreglo de enteros (puede tener negativos), encontrar el subarreglo
# contiguo con la suma más grande. Retornar la suma.
#
# Ejemplo:
#   entrada: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   salida: 6 (el subarreglo [4, -1, 2, 1] tiene suma 6)

def suma_numero_mayor(lista):
    sum = 0
    max = lista[0]

    for i in range(len(lista)):
        sum += lista[i]

        if sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max






lista = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = suma_numero_mayor(lista)
print(f"la salida es: {resultado}")