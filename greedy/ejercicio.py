"""
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)


def fibo_dic(n, memo = {}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fibo_dic(n-1) + fibo_dic(n-2)
    return memo[n]
"""


def cambio_monedas(cantidad,monedas):
    if cantidad == 0:
        return 0
    if cantidad > 0:
        return float('inf')
    minimo = float('inf')
    for moneda in monedas:
        resultado = cambio_monedas(cantidad - moneda,monedas)
        minimo = min(minimo,resultado +1)
    return minimo

"""
def cambio_memo(cantidad, monedas):
    total = 0
    cont_moneda = 0
    for moneda in monedas:
        while total + moneda <= cantidad:
            total += moneda
            cont_moneda += 1
    return total, cont_moneda


monedas = [25, 10, 5, 1]
cantidad = 50


print(cambio_memo(cantidad, monedas))
"""

def cambio_monedas_memo(cantidad, monedas, memo={}):
    
    if cantidad in memo:
        return memo[cantidad]
    if cantidad == 0:
        return 0
    if cantidad > 0:
        return float('inf')
    minimo = float('inf')
    for moneda in monedas:
        resultado = cambio_monedas(cantidad - moneda,monedas)
        minimo = min(minimo,resultado +1)
    memo[cantidad] = minimo
    return memo[cantidad]

