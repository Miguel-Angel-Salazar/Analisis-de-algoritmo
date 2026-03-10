"""
 Dada una lista de intervalos, combina los que se superponen.
#
# Ejemplo:
#   intervalos = [(1,3), (2,6), (8,10), (15,18)]
#   Respuesta: [(1,6), (8,10), (15,18)]
#
#   intervalos = [(1,4), (4,5)]
#   Respuesta: [(1,5)]  # Se tocan en el punto 4
"""
def solucion_comprimir_intervalos(intervalos):
    if not intervalos:
        return []
    
    # Ordenar por inicio
    intervalos = sorted(intervalos, key=lambda x: x[0])
    
    resultado = [list(intervalos[0])]
    
    for inicio, fin in intervalos[1:]:
        ultimo = resultado[-1]
        
        if inicio <= ultimo[1]:  # Se superponen o tocan
            ultimo[1] = max(ultimo[1], fin)  # Extender
        else:
            resultado.append([inicio, fin])
    
    return [tuple(i) for i in resultado]
intervalos = [(1,3), (2,6), (8,10), (15,18)]
print(solucion_comprimir_intervalos(intervalos))