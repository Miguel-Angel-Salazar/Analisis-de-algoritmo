# Calcular base^exponente usando recursión por fuerza bruta.
# No usar el operador ** ni la función pow().
#
# Ejemplo:
#   entrada: base=2, exponente=10
#   salida: 1024

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente -1)



base = 2
exponente = 10

print(f"la potencia es de: {potencia(base,exponente)}")