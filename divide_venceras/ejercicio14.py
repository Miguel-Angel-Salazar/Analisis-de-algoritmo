#hayar la maxima resta entre los elementos de la lista
# ----------- SOLUCIÓN 1: SUBLISTAS -----------

def max_diferencia_sublistas(lista):
    if len(lista) < 2:
        return 0

    mitad = len(lista) // 2
    izq = lista[:mitad]
    der = lista[mitad:]

    max_izq = max_diferencia_sublistas(izq)
    max_der = max_diferencia_sublistas(der)

    min_izq = min(izq)
    max_der_val = max(der)

    max_cruzado = max_der_val - min_izq

    return max(max_izq, max_der, max_cruzado)


# ----------- SOLUCIÓN 2: ÍNDICES -----------

def max_diferencia_indices(lista, inicio, fin):
    if inicio == fin:
        return 0, lista[inicio], lista[inicio]

    mitad = (inicio + fin) // 2

    max_izq, min_izq, max_izq_val = max_diferencia_indices(lista, inicio, mitad)
    max_der, min_der, max_der_val = max_diferencia_indices(lista, mitad + 1, fin)

    max_cruzado = max_der_val - min_izq
    max_total = max(max_izq, max_der, max_cruzado)

    return max_total, min(min_izq, min_der), max(max_izq_val, max_der_val)


# ----------- PRUEBA -----------

lista = [2,3,10,6,4,8,1]

res_sublistas = max_diferencia_sublistas(lista)
res_indices, _, _ = max_diferencia_indices(lista, 0, len(lista)-1)

print("Sublistas:", res_sublistas)
print("Índices:", res_indices)