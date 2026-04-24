#Determinar si una lista está ordenada de menor a mayor usando DyV
def esta_ordenado(lista):
    
    if len(lista) <= 1:
        return True
    
    mitad = len(lista)//2
    izq = lista[:mitad]
    der = lista[mitad:]
    
    orden_izq = esta_ordenado(izq)
    orden_der = esta_ordenado(der)
    
    # AQUÍ VIENE LO IMPORTANTE
    if orden_izq and orden_der and izq[-1] <= der [0]:
        return True
    else:
        return False
    
lista1=[1,2,3,4]  
lista2=[1,3,2,4] 
print(esta_ordenado(lista1))
print(esta_ordenado(lista2))