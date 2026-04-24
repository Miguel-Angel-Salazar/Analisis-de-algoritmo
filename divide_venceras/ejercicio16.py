# menores a x

def menores_que_x(lista, x, inicio, fin):
    if inicio > fin:
        return inicio
    
    mitad = (inicio + fin) // 2
    
    if lista[mitad] < x:
        return menores_que_x(lista, x, mitad + 1, fin)
    else:
        return menores_que_x(lista, x, inicio, mitad - 1)


lista = [1,2,3,5,7]
x = 5
print(menores_que_x(lista, x, 0, len(lista)-1))  # O(log n)

def menores_que_x_sublista(lista, x, offset=0):
    if len(lista) == 0:
        return offset
    
    mitad = len(lista) // 2
    
    if lista[mitad] < x:
        return menores_que_x_sublista(lista[mitad+1:], x, offset + mitad + 1)
    else:
        return menores_que_x_sublista(lista[:mitad], x, offset)


lista = [1,2,3,5,7]
x = 5
print(menores_que_x_sublista(lista, x))  # O(n)