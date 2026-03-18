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