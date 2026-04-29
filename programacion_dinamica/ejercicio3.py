def contar_monedas(monedas,monto):
    if monto == 0:
        return 0
    if monto < 0:
        return float('inf')
    
    minimo = float('inf')

    for moneda in monedas:
        resultado = contar_monedas(monedas, monto - monedas)
        minimo = min(minimo,resultado +1)
    return minimo

def contar_memo(monedas, monto, memo = {}):

    if monto in memo:
        return memo[monto]
    if monto < 0:
        return float('inf')

    minimo = float('inf')
    for moneda in monedas:
        resultado = contar_memo(monedas, monto - moneda, memo)
        minimo = min(minimo, resultado + 1)

    memo[monto] = minimo
    return memo[monto]