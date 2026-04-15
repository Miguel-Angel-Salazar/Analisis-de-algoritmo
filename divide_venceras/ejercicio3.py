#sumar todos los elementos del arreglo

def suma_divide_venceras(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]
    
    medio = (inicio + fin) // 2
    
    izquierda = suma_divide_venceras(arr, inicio, medio)
    derecha = suma_divide_venceras(arr, medio + 1, fin)
    
    return izquierda + derecha

arr = [1, 2, 3, 4, 5]
resultado = suma_divide_venceras(arr, 0, len(arr) - 1)
print(resultado)  

    