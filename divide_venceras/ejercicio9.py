# Dado un arreglo ordenado, encuentra la posición de un número.



def busqueda_binaria(lista,objetivo,inicio,fin):
    if inicio > fin:
        return -1
    
    mitad = (inicio + fin) // 2

    if objetivo == lista[mitad]:
        return mitad
    
    elif objetivo < lista[mitad]:
        return busqueda_binaria(lista, objetivo,inicio, mitad -1)
    else:
        return busqueda_binaria(lista, objetivo, mitad + 1, fin)
    
lista = [1,2,3,4,5,6,7,8,9]
objetivo = 7

print(busqueda_binaria(lista,objetivo, 0, len(lista)-1))

def busqueda_binaria_sublista(lista,objetivo):
    if len(lista) == 0:
        return -1
    
    mitad = len(lista)// 2
    derecha = lista[mitad +1 :]
    izquierda = lista[:mitad]
    

    if objetivo == lista[mitad]:
        return mitad
    elif objetivo < lista[mitad]:
        return busqueda_binaria_sublista(izquierda, objetivo)
        
    else:
        resultado = busqueda_binaria_sublista(derecha, objetivo)
        if resultado == -1:
            return -1
        else:
            return resultado + (mitad +1)
    

lista = [1,2,3,4,5,6,7,8,9]
objetivo = 7
    
print(busqueda_binaria_sublista(lista, objetivo))

def busqueda_binaria_sublista_booleano(lista,objetivo):
    if len(lista) == 0:
        return False
    
    mitad = len(lista)// 2
    derecha = lista[mitad:]
    izquierda = lista[:mitad]
    

    if objetivo == lista[mitad]:
        return True
    elif objetivo < lista[mitad]:
        return busqueda_binaria_sublista(izquierda, objetivo)
        
    else:
        return busqueda_binaria_sublista(derecha, objetivo)
        
    

lista = [1,2,3,4,5,6,7,8,9]
objetivo = 7
    
print(busqueda_binaria_sublista(lista, objetivo))