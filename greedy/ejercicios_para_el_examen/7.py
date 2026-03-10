"""
# Eres un gerente y tienes varias reuniones propuestas para hoy.
# Cada reunión tiene una hora de inicio y fin.
# Quieres asistir al MÁXIMO número de reuniones posible.
#
# Ejemplo:
#   reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]
#   Respuesta: 3 reuniones → [(9, 10), (10, 11), (12, 14)]
"""
def solucion_max_reuniones(reuniones):
    if not reuniones:
        return []
    
    # Ordenar por hora de fin
    reuniones_ordenadas = sorted(reuniones, key=lambda x: x[1])
    
    seleccionadas = [reuniones_ordenadas[0]]
    ultimo_fin = reuniones_ordenadas[0][1]
    
    for inicio, fin in reuniones_ordenadas[1:]:
        if inicio >= ultimo_fin:
            seleccionadas.append((inicio, fin))
            ultimo_fin = fin
    
    return seleccionadas
reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]

print(solucion_max_reuniones(reuniones))