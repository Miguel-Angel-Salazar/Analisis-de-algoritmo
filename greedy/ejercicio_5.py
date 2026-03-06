def recorrido_carro(capacidad_carro, estaciones):
    estaciones_ordenadas = sorted(estaciones)
    kilometraje_carro = 0
    capacidad_actual = capacidad_carro
    estacion_anterior = 0  

    for estacion in estaciones_ordenadas:
        distancia_a_siguiente = estacion - estacion_anterior

        if capacidad_actual >= distancia_a_siguiente:
            kilometraje_carro += distancia_a_siguiente
            capacidad_actual -= distancia_a_siguiente
            capacidad_actual = capacidad_carro
        else:
            kilometraje_carro += capacidad_actual
            capacidad_actual = 0
            print(f"El carro se quedó sin combustible antes de la estación {estacion}")
            break

        estacion_anterior = estacion

    return kilometraje_carro


estaciones = [42, 8, 12, 21]
capacidad_carro = 10
print(recorrido_carro(capacidad_carro, estaciones))