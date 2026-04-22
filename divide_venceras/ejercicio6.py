def invertir(lista):
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    
    if derecha:
        return invertir(derecha) + invertir(izquierda)
    else:
        return invertir(izquierda)

lista = [6,3,5,4,8,1]
print(invertir(lista))

#_____________________________________

def inveritir_sin_div(lista, inicio, fin):
    if inicio >= fin:
        return
    lista[inicio], lista[fin] = lista[fin], lista[inicio]
    inveritir_sin_div(lista, inicio +1, fin -1)
    
lista1 = [6,3,5,4,8,1,0,9]
inveritir_sin_div(lista1,0, len(lista1) -1)
print(lista1)