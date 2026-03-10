def cambio_greedy(monedas, monto):

    monedas = sorted(monedas, reverse=True)
    resultado = []

    for moneda in monedas:

        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)

    return resultado

monedas = [1, 5, 10, 25]
monto = 63

print(cambio_greedy(monedas, monto))