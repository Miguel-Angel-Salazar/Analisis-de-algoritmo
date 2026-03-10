"""
 Tienes un camión con capacidad máxima de peso.
# Hay varias cajas, cada una con un peso y un valor.
# NO puedes partir las cajas (a diferencia de la mochila fraccionaria).
# Maximiza el valor total que puedes cargar.
#
# Nota: Este problema NO siempre se resuelve óptimamente con Greedy,
#       pero intenta una aproximación greedy y analiza cuándo falla.
#
# Ejemplo:
#   capacidad = 10
#   cajas = [(5, 10), (4, 40), (6, 30), (3, 50)]  # (peso, valor)
#   Greedy por valor/peso: selecciona (3,50) y (4,40) → valor = 90

"""
def solucion_llenar_camion(capacidad, cajas):

    cajas_con_ratio = [(p, v, v/p, i) for i, (p, v) in enumerate(cajas)]
    cajas_con_ratio.sort(key=lambda x: x[2], reverse=True)
    
    valor_total = 0
    seleccionadas = []
    
    for peso, valor, ratio, idx in cajas_con_ratio:
        if peso <= capacidad:
            seleccionadas.append((peso, valor))
            valor_total += valor
            capacidad -= peso
    
    return valor_total, seleccionadas

capacidad = 10
cajas = [(5, 10), (4, 40), (6, 30), (3, 50)]
print(solucion_llenar_camion(capacidad,cajas))