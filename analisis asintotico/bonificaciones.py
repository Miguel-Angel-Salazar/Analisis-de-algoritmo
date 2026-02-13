def encontrar_pareja(lista, objetivo):
    visitado = set()

    for valor in lista:
        if objetivo - valor in visitado:
            return True
        visitado.add(valor)
    return False

print("ejemplo")
lista = [100,50,300,220,10]
objetivo = 270

print(f"lista: {lista}, objetivo: {objetivo} -> los cuales son : {encontrar_pareja(lista,objetivo)} ")
