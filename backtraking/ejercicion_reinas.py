def n_reinas(n):
    solucion = [-1] * n
    resultado = []          
    def backtraking(fila):
        if fila == n:
            resultado.append(solucion.copy())
            return

        for columna in range(n):
            valido = True
            for i in range(fila):
                if solucion[i] == columna or abs(solucion[i] - columna) == abs(i - fila):
                    valido = False
                    break
            if valido:
                solucion[fila] = columna
                backtraking(fila + 1)
                solucion[fila] = -1
    backtraking(0)
    return resultado    
print(n_reinas(4))