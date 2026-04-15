def contar_inversiones(arr):
    if len(arr) <= 1:
        return arr, 0

    medio = len(arr) // 2

    izq, inv_izq = contar_inversiones(arr[:medio])
    der, inv_der = contar_inversiones(arr[medio:])

    i = 0
    j = 0
    inv = inv_izq + inv_der
    resultado = []

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            inv += len(izq) - i
            j += 1

    # agregar lo que sobra (sin extend)
    while i < len(izq):
        resultado.append(izq[i])
        i += 1

    while j < len(der):
        resultado.append(der[j])
        j += 1

    return resultado, inv
