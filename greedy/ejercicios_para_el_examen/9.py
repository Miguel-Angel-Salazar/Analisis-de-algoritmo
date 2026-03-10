"""
# Vas a hacer un viaje en carretera. Tu tanque tiene capacidad para
# recorrer K kilómetros. Hay estaciones de gasolina en ciertas posiciones.
# Quieres hacer el MÍNIMO número de paradas para llegar al destino.
#
# Ejemplo:
#   distancia_total = 25
#   capacidad_tanque = 10  # km que puedes recorrer con tanque lleno
#   estaciones = [5, 8, 15, 22]  # posiciones de las estaciones
#   Respuesta: 2 paradas (en km 8 y km 22)
"""

def solucion_min_paradas_v2(distancia_total, capacidad, estaciones):
    estaciones = [0] + sorted(estaciones) + [distancia_total]
    paradas = []
    combustible = capacidad
    
    for i in range(1, len(estaciones)):
        distancia = estaciones[i] - estaciones[i-1]
        
        if distancia > capacidad:
            return -1  # Imposible
        
        if distancia > combustible:
            # Parar en la estación anterior
            paradas.append(estaciones[i-1])
            combustible = capacidad
        
        combustible -= distancia
    
    return paradas

distancia_total = 25
capacidad_tanque = 10  
estaciones = [5, 8, 15, 22] 
print(solucion_min_paradas_v2(distancia_total,capacidad_tanque,estaciones))