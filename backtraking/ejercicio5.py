"""
generar todas las cadenas binarias de longitud n, donde no hayas 1s consecutivos
ejemplo
n=3
001,000,010,100,101
"""
def cadenas_binarias(n):
    resultado = []
    cadena = [''] * n

    def backtracking(posicion):
        if posicion == n:
            resultado.append(''.join(cadena))
            return

        cadena[posicion] = '0'
        backtracking(posicion + 1)

        if posicion == 0 or cadena[posicion - 1] != '1':
            cadena[posicion] = '1'
            backtracking(posicion + 1)

    backtracking(0)
    return resultado

print(cadenas_binarias(3))
