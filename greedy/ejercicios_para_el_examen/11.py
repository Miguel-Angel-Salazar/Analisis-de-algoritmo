"""
Una estación de tren tiene trenes que llegan y salen a diferentes horas.
# ¿Cuál es el MÍNIMO número de plataformas necesarias para que
# ningún tren tenga que esperar?
#
# Ejemplo:
#   llegadas =  [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
#   salidas  =  [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
#   Respuesta: 3 plataformas
#
#   Explicación: A las 11:00 hay 3 trenes simultáneos
#   (el de 9:40 sale a 12:00, el de 9:50 sale a 11:20, y llega uno a 11:00)


"""

def solucion_min_plataformas(llegadas, salidas):
    # Crear eventos: (tiempo, tipo) donde tipo=1 es llegada, tipo=-1 es salida
    eventos = []
    for t in llegadas:
        eventos.append((t, 1))   # Llegada
    for t in salidas:
        eventos.append((t, -1))  # Salida
    
    # Ordenar por tiempo. Si empatan, procesar salidas primero (-1 < 1)
    eventos.sort(key=lambda x: (x[0], x[1]))
    
    plataformas_actuales = 0
    max_plataformas = 0
    
    for tiempo, tipo in eventos:
        plataformas_actuales += tipo
        max_plataformas = max(max_plataformas, plataformas_actuales)
    
    return max_plataformas

llegadas =  [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
salidas  =  [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
print(solucion_min_plataformas(llegadas,salidas))