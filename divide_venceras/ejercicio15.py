#mismo numeros

def igualdad(lista):
    if len(lista) == 1:
        return True
    
    mitad = len(lista) // 2

    izq = lista[:mitad]
    der = lista[mitad:]

    izq_ok = igualdad(izq)
    der_ok = igualdad(der)

    if izq_ok and der_ok and izq[-1] == der[0]:
        return True
    else:
        return False


lista1=[2,2,2,2,2]
lista2=[2,2,3,2,2]
print(igualdad(lista1))
print(igualdad(lista2))