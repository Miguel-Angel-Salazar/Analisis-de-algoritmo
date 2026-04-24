#Encuentra el máximo elemento de una lista usando Divide y Vencerás (NO iterativo).
def max_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    
    mitad = len(lista) // 2

    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    max_izq = max_elemento(izquierda)
    max_der = max_elemento(derecha)

    if max_der > max_izq:
        return max_der
    else:
        return max_izq


lista = [3,1,7,9,5,2,8,6]
print(max_elemento(lista))