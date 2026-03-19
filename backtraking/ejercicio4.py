def generar_parentesis(n):
    if n <= 0:
        return []

    resultado = []

    def backtrack(cadena, abiertos, cerrados):
        if len(cadena) == 2 * n:
            resultado.append(cadena)
            return

        if abiertos < n:
            backtrack(cadena + "(", abiertos + 1, cerrados)

        if cerrados < abiertos:
            backtrack(cadena + ")", abiertos, cerrados + 1)

    backtrack("", 0, 0)
    return resultado


if __name__ == "__main__":
    print(generar_parentesis(3))



#______________________________________________________

def generar_parentesis_corchetes(n):
    resultado = []

    def backtrack(cadena, abiertos_p, cerrados_p, abiertos_c, cerrados_c, pila):
        if len(cadena) == 4 * n:
            resultado.append(cadena)
            return

        if abiertos_p < n:
            backtrack(
                cadena + "(",
                abiertos_p + 1,
                cerrados_p,
                abiertos_c,
                cerrados_c,
                pila + "("
            )

        if abiertos_c < n:
            backtrack(
                cadena + "[",
                abiertos_p,
                cerrados_p,
                abiertos_c + 1,
                cerrados_c,
                pila + "["
            )

        if cerrados_p < abiertos_p and pila and pila[-1] == "(":
            backtrack(
                cadena + ")",
                abiertos_p,
                cerrados_p + 1,
                abiertos_c,
                cerrados_c,
                pila[:-1]
            )

        if cerrados_c < abiertos_c and pila and pila[-1] == "[":
            backtrack(
                cadena + "]",
                abiertos_p,
                cerrados_p,
                abiertos_c,
                cerrados_c + 1,
                pila[:-1]
            )

    backtrack("", 0, 0, 0, 0, "")
    return resultado

if __name__ == "__main__":
    print(generar_parentesis_corchetes(2))
