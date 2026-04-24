

def segundo_max1(lista):
    if len(lista) <= 2:
        if len(lista) == 1:
            return lista[0], float('-inf')  
        if lista[0] > lista[1]:
            return lista[0], lista[1]
        else:
            return lista[1], lista[0]

    mitad = len(lista) // 2

    izq = lista[:mitad]
    der = lista[mitad:]

    max_izq, segundo_izq = segundo_max1(izq)
    max_der, segundo_der = segundo_max1(der)

    if max_izq > max_der:
        total_max = max_izq
        segundo_total = max(max_der, segundo_izq)
    else:
        total_max = max_der
        segundo_total = max(max_izq, segundo_der)

    return total_max, segundo_total


lista = [1, 2, 3, 9, 5, 6]
print(segundo_max1(lista)[1])