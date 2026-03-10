def antenas(ciudades):

    ciudades.sort()
    i = 0
    n = len(ciudades)
    antenas = []

    while i < n:

        start = ciudades[i]

        pos = start + 4
        antenas.append(pos)

        while i < n and ciudades[i] <= pos + 4:
            i += 1

    return antenas

ciudades = [1,2,3,6,9,11,12]
print(antenas(ciudades))


#__________________________________________________________________

#con lugares de ciudades
def colocar_antenas(ciudades):

    ciudades.sort()
    n = len(ciudades)
    i = 0
    antenas = []

    while i < n:

        # ciudad más a la izquierda no cubierta
        start = ciudades[i]

        # avanzar mientras esté dentro de start+4
        while i < n and ciudades[i] <= start + 4:
            i += 1

        # la antena se pone en la última ciudad válida
        antena = ciudades[i-1]
        antenas.append(antena)

        # ahora saltamos todas las ciudades cubiertas por esa antena
        while i < n and ciudades[i] <= antena + 4:
            i += 1

    return antenas
ciudades = [1,2,3,6,9,11,12]
print(colocar_antenas(ciudades))