def mochila_fraccionaria(capacidad, objetos):
    objetos_con_ratio = [(p, v, p/v) for p, v in objetos]
    objetos_con_ratio.sort(key= lambda x: x[2], reverse=True)

    valor_total = 0
    objetos_almacenados = []

    for peso, valor, ratio in objetos_con_ratio:
        if capacidad >= peso:
            valor_total += valor
            capacidad -= peso
            objetos_almacenados.append((peso, valor, 1))
        elif capacidad > 0:
            fraccion = capacidad / peso
            valor_total += valor * fraccion
            objetos_almacenados.append((peso, valor, fraccion))
            break

    return objetos_almacenados, valor_total


peso = [20, 40]
valor = [10, 30]
capacidad = 100

objetos = list(zip(peso, valor))

resultado, valor_total = mochila_fraccionaria(capacidad, objetos)

print("Objetos almacenados:", resultado)
print("Valor total:", valor_total)