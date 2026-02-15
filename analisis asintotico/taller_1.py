"""
Dado un arreglo de enteros, encontrar el elemento que aparece más de n/2 veces.
Se garantiza que siempre existe un elemento mayoritario.

Ejemplo:
entrada: [3, 3, 4, 2, 3, 3, 5, 3, 3]
salida: 3 (aparece 6 veces, n/2 = 4.5)
"""

def numero_repetido(lista):

    for posicion, valor in enumerate(lista):
        contador = 0
        for i in lista:
            if valor == i:
                contador += 1
        if contador > len(lista) / 2:
            return valor


lista = [3, 3, 4, 2, 3, 3, 5, 3, 3]

resultado = numero_repetido(lista)
print(f"salida es: {resultado}")