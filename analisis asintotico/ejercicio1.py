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
