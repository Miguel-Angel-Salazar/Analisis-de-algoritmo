def validar_orden(lista):
    if len(lista) == 1:
        return True
    
    mitad = len(lista) // 2

    izq = lista[:mitad]
    der = lista[mitad:]

    orden_izq= validar_orden(izq)
    orden_der = validar_orden(der)

    if orden_izq and orden_der and izq[-1] <= der[0]:
        return True
    else:
        return False

    
lista1=[1,5,9.,7]
lista2 = [4,5,6,]
print(validar_orden(lista1))
print(validar_orden(lista2))