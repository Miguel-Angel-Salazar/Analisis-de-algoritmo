def suma_sublista(lista, objetivo):
    n = len(lista)

    for inicio in range(n):
        suma = 0
        for fin in range(inicio, n):
            suma += lista[fin]

            if suma == objetivo:
                return True

    return False