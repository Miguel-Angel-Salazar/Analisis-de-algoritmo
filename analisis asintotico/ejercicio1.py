def funcion(n):
    print("hola")
    if n ==1:
        print(n)
    for i in range(0, n): # se ejecuta n veces porque empieza desde el 0
        print("adios")

# si hay un ciclo o varios y depende de la entrada significa que va a ser de complejidad lineal
# si el ciclo no depende de la entrada por lo tanto es constante
# cuanto llegamos al limite seria el caso Big O, el peor caso de todos por ser probado 
# para saber cual es el caso Big O lo unico que hago es eliminar nuestras constante y evaluar en esos terminos
# si se llega el caso en el que una de las funciones pertenece a la otra se pueden juntar las dos f(n) = n**2 y g(n) = n; la funcion completa es n**2 + n, como pertenecen se agrupan

"""
ejemplo

f(n) =  n**2 + n

cual es la complejidad = n**2 (se pudo agrupar n en n**2)
cual es el tamaño de la entrada =
cuantas operaciones se hacen =


ejemplo 2

operacion(n)
i = 1
while i < n
    if XXXXXX
    i = i * 2

su complejidad es logaritmica ya que como se encuentra el while y el resultado final se puede obsevsar que i * 2, y analizando la condicion del while;
podemos observar que llegara mas rapido que si fuera un ciclo for, por lo tanto es logaritmico
"""

# siempre que se ve algo recursivo que se llame una unica vez, su complejidad es lineal O(n)