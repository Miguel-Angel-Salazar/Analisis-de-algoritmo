def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivote = arr[0]
    menores = [x for x in arr[1:] if x <= pivote]
    mayor = [x for  x in arr[1:] if x > pivote]

    return quick_sort(menores)+ [pivote] + quick_sort(mayor)

print(quick_sort([5,10,4,1,3,7]))


#______________________________________

def quick_select(arr, k):
    # Si el arreglo tiene un solo elemento, ese es el resultado
    if len(arr) == 1:
        return arr[0]
    
    # Elegimos el primer elemento como pivote
    pivote = arr[0]
    
    # Creamos una lista con los elementos menores o iguales al pivote
    menores = [x for x in arr[1:] if x <= pivote]
    
    # Creamos una lista con los elementos mayores al pivote
    mayores = [x for x in arr[1:] if x > pivote]

    # Si k está dentro de la cantidad de elementos menores,
    # seguimos buscando en ese subarreglo
    if k <= len(menores):
        return quick_select(menores, k)
    
    # Si k corresponde exactamente a la posición del pivote,
    # entonces el pivote es el k-ésimo menor
    elif k == len(menores) + 1:
        return pivote
    
    # Si k es mayor, buscamos en los elementos mayores,
    # ajustando k restando los elementos ya descartados
    else:
        return quick_select(mayores, k - len(menores) - 1)


# Llamamos a la función con k=2 (segundo menor)
print(quick_select([5,10,4,1,3,7], 2))