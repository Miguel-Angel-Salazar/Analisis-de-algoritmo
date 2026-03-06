def mochila_1(capacidad = int, peso= [], valor =[]):
    contador_peso = 0
    contador_valor = 0
    while contador_peso < capacidad:
        for i in range(len(peso)):
            contador_peso += peso[i]
            contador_valor += valor[i]

            if contador_peso > capacidad:
                contador_peso -= peso[i]
                contador_valor -= valor[i]
                restante = capacidad - contador_peso
                fraccion = restante / peso[i]
                contador_valor += valor[i] * fraccion
                return contador_valor, contador_peso
            
            elif contador_peso == capacidad:
                return contador_valor, contador_peso
    return contador_valor, contador_peso


peso = [20,40]
valor = [10,30]
capacidad = 100

resultado, contador_peso = mochila_1(capacidad, peso, valor)

print(resultado, contador_peso)