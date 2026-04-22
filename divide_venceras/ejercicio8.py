def encontrar_piso(lista, valor):
    if len(lista) == 1:
        return lista[0] if lista[0] <= valor else None

    mitad = len(lista) // 2
    mid_val = lista[mitad]

    if mid_val == valor:
        return mid_val

    if mid_val > valor:
        return encontrar_piso(lista[:mitad], valor)

    # mid_val < valor
    der = encontrar_piso(lista[mitad:], valor)

    if der is not None:
        return der
    else:
        return mid_val
    
lista = [1,3,6,8]
valor = 7

print(encontrar_piso(lista, valor))