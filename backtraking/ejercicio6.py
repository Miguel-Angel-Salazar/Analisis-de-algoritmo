"""
generar todas las cadenas con "a" y "b" de longitud n, donde no haya mas de 2 consecutivos
ejemplo
n=3
aaa, aab, aba, abb, baa, bab, bba, bbb
"""
def cadenas_binarias(n):
    resultado = []

    def backtracking(cadena, ultima, consecutivos):
        if len(cadena) == n:
            resultado.append(cadena)
            return


        if ultima != 'a' or consecutivos < 2:
            backtracking(cadena + 'a','a',consecutivos + 1 if ultima == 'a' else 1)

        if ultima != 'b' or consecutivos < 2:
            backtracking(cadena + 'b','b',consecutivos + 1 if ultima == 'b' else 1)

    backtracking("", "", 0)
    return resultado

print(cadenas_binarias(3))