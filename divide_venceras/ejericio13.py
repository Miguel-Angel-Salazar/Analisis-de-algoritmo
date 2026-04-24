
#hacer el sub arreglo el cual tenga la mayor suma posible

def max_subarray(lista):
    if len(lista) == 1:
        return lista[0]
    
    mitad = len(lista) // 2
    
    izq = lista[:mitad]
    der = lista[mitad:]
    
    max_izq = max_subarray(izq)
    max_der = max_subarray(der)
    
    # Caso cruzado
    suma = 0
    max_izq_cruz = float('-inf')
    
    for i in range(mitad - 1, -1, -1):
        suma += lista[i]
        max_izq_cruz = max(max_izq_cruz, suma)
    
    suma = 0
    max_der_cruz = float('-inf')
    
    for i in range(mitad, len(lista)):
        suma += lista[i]
        max_der_cruz = max(max_der_cruz, suma)
    
    max_cruzado = max_izq_cruz + max_der_cruz
    
    return max(max_izq, max_der, max_cruzado)

lista = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(lista))