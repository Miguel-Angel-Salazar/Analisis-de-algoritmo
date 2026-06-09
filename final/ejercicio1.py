def generar_playlist(history):
    frecuencia = {}
    posicion = {}
    
    for i, j in enumerate(history):
      frecuencia[j] = frecuencia.get(j, 0) +1
      posicion[j] = i
    
    canciones = []
    
    for j in frecuencia:
      valor = frecuencia[j] - posicion[j]
      
      canciones.append((valor, frecuencia[j],j))
      
    canciones.sort(reverse = True)
      
    playlist = ""
      
    for _,_,j in canciones:
        playlist += j
        
    return playlist  
    
history = "ADDBBBCDAA"
print(generar_playlist(history))