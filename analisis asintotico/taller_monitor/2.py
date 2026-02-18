def ordenamineto(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] =lista[j + 1], lista[j]
    return lista


lista = [5, 1, 4, 2, 8]
print(f"la lista ordenada es: {ordenamineto(lista)}")


def ordenado(lista):
    for i in range(len(lista)):
        for j in range(i + 1,len(lista)):
            primero = lista[i]
            segundo = lista[j]
            if primero > segundo:
                lista[i] = segundo
                lista[j] = primero
    return lista


lista1 = [5, 1, 4, 2, 8]
print(f"la lista ordenada es: {ordenado(lista1)}")
