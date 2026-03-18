def encontrar_combinaciones(lista, objetivo):
    resultado = []

    def backtrack(indice, suma_actual, camino):
 
        if suma_actual == objetivo:
            resultado.append(camino.copy())
            return
        
        if suma_actual > objetivo or indice >= len(lista):
            return

        camino.append(lista[indice])
        backtrack(indice + 1, suma_actual + lista[indice], camino)

        camino.pop()
        backtrack(indice + 1, suma_actual, camino)

    backtrack(0, 0, [])
    return resultado


lista = [1, 2, 5, 6, 8]
objetivo = 7

print(encontrar_combinaciones(lista, objetivo))