# Cuenta cuántas veces aparece un número en una lista (NO usar .count())

def contar(lista, objetivo):
    if len(lista) == 1:
        if lista[0] == objetivo:
            return 1
        else:
            return 0
    
    mitad = len(lista) // 2

    izq = lista[:mitad]
    der = lista[mitad:]

    cont_izq = contar(izq, objetivo)
    cont_der = contar(der, objetivo)

    return cont_izq + cont_der

lista = [1,3,2,1,4,2,5,1] 
objetivo = 3
print(contar(lista,objetivo))

#_____________________________________________________
def contar1(lista, objetivo):
    if len(lista) == 0:
        return 0
    
    if len(lista) == 1:
        if lista[0] == objetivo:
            return 1
        else:
            return 0
    
    mitad = len(lista) // 2
    izq = lista[:mitad]
    der = lista[mitad:]
    
    return contar1(izq, objetivo) + contar1(der, objetivo)


def mas_frecuente(lista):
    if len(lista) == 1:
        return lista[0]
    
    mitad = len(lista) // 2
    izq = lista[:mitad]
    der = lista[mitad:]
    
    # Resolver cada mitad
    izq_elem = mas_frecuente(izq)
    der_elem = mas_frecuente(der)
    
    # Combinar: contar en TODA la lista
    cont_izq = contar1(lista, izq_elem)
    cont_der = contar1(lista, der_elem)
    
    if cont_izq > cont_der:
        return izq_elem
    else:
        return der_elem


# Prueba
lista = [1,3,2,1,4,5,1]
print(mas_frecuente(lista))