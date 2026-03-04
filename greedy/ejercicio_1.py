import heapq
#leer el elemento es constante
#sacar o insertar elemento es logaritmico
# para invertir el valor si lo quiero poner como en orden maximo multiplicamos por -1
datos = [ 5,3,8,1,2,9,4]

heapq.heapify(datos)
print(datos) # los padres son menores que sus hijos, no ordena de menor a mayor 
heapq.heappush(datos, 0) #insertar 
print(datos)
min = heapq.heappop(datos)#sacar
print(min)
print(datos)
resultado = heapq.heappushpop(datos, 10)#inserta primero y luego saca el valor de la raiz del arbol, es mas eficiente que los demas a pesar
#de ser de la misma complejidad
print(resultado)
print(datos)


