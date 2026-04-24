#Dada una lista, devuelve la suma total usando Divide y Vencerás.

def suma(lista):
    if len(lista) == 1:
        return lista[0]
    
    mitad= len(lista) // 2

    left = lista[:mitad]
    right = lista[mitad:]

    sum_l = suma(left)
    sum_r = suma(right)

    return sum_l + sum_r

lista = [1,2,3,4]
print(suma(lista))