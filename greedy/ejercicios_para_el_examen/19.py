def cables_internet(casas, cables):

    cables.sort(key=lambda x: x[2])
    
    grupos = {c: c for c in casas}
    
    resultado = []
    costo_total = 0

    for casa1, casa2, costo in cables:
        
        if grupos[casa1] != grupos[casa2]:
            
            grupo_viejo = grupos[casa2]
            
            for c in grupos:
                if grupos[c] == grupo_viejo:
                    grupos[c] = grupos[casa1]
            
            resultado.append((casa1, casa2, costo))
            costo_total += costo

    return costo_total, resultado


casas = ["A","B","C","D"]

cables = [
("A","B",4),
("A","C",2),
("B","C",1),
("B","D",5),
("C","D",8)
]

print(cables_internet(casas, cables))

#Ordenar los cables por costo y seleccionar siempre el más barato
#que conecte dos casas que aún no estén conectadas entre sí.