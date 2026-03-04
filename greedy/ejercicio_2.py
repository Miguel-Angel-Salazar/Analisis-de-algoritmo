import heapq
pacientes =[
("Juan",1),
("Maria",3),
("fernando", 2),
("luisa",6),
("blast",1)]

hospital = []
orden = 0  


for nombre, prioridad in pacientes:
    heapq.heappush(hospital, (prioridad, orden, nombre))
    orden += 1


while hospital:
    prioridad, orden_llegada, nombre = heapq.heappop(hospital)
    print(f"Atendiendo a {nombre}, con llegada {orden_llegada}, con prioridad {prioridad}")