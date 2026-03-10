"""
Dadas dos cadenas:

s: cadena de entrada
p: patrón
Implementa un algoritmo que determine si el patrón coincide completamente con la cadena, usando las siguientes reglas de comodines:

'?' coincide con exactamente un carácter cualquiera.
'*' coincide con cualquier secuencia de caracteres (incluyendo la secuencia vacía).
La coincidencia debe cubrir toda la cadena de entrada (no coincidencias parciales).

Ejemplo 1 Entrada: s = "aa", p = "a" Salida: false Explicación: "a" no cubre toda la cadena "aa".

Ejemplo 2 Entrada: s = "aa", p = "*" Salida: true Explicación: '*' puede representar "aa".

Ejemplo 3 Entrada: s = "cb", p = "?a" Salida: false Explicación: '?' casa con 'c', pero 'a' no casa con 'b'.
"""
def coincide_patron(cadena, patron):

    posicion_cadena = 0
    posicion_patron = 0

    posicion_estrella = -1
    coincidencia = 0

    while posicion_cadena < len(cadena):

        if (posicion_patron < len(patron) and
            (patron[posicion_patron] == cadena[posicion_cadena] or
             patron[posicion_patron] == '?')):

            posicion_cadena += 1
            posicion_patron += 1

        elif posicion_patron < len(patron) and patron[posicion_patron] == '*':
            posicion_estrella = posicion_patron
            coincidencia = posicion_cadena
            posicion_patron += 1

        elif posicion_estrella != -1:
            posicion_patron = posicion_estrella + 1
            coincidencia += 1
            posicion_cadena = coincidencia

        else:
            return False

    while posicion_patron < len(patron) and patron[posicion_patron] == '*':
        posicion_patron += 1

    return posicion_patron == len(patron)


cadena = "aa"
patron = "*"

print(coincide_patron(cadena, patron))
