"""
def clave_candado(combinacion=int):

    contraseña = input("Ingrese su contraseña: ")

    for i in range(1):
        if combinacion == contraseña:
            print("el candado abre")
        else:
            print("contraseña incorrecta")

resultado = clave_candado()
print(resultado)
"""
# _____________________________________________________________________
"""
contraseña = input("Ingrese su contraseña: ")

intentos = 0

for i in range(0,1000):
    clave_generada = str(i).zfill(3) 
    intentos += 1

    if clave_generada == contraseña:
        print("el candado abre")
        print(f"la clave es {clave_generada} y se intentó {intentos} veces")
        break
    
"""
"""
contraseña = input("Ingrese su contraseña")
n = len(contraseña)
intentos = 0

for i in range(0,10**n):
    clave_generada = str(i).zfill(n) 
    intentos += 1

    if clave_generada == contraseña:
        print("el candado abre")
        print(f"la clave es {clave_generada} y se intentó {intentos} veces")
        break

"""

clave = input("Ingrese la clave: ")
n = len(clave)

intentos = 0
prefijo = ""

for posicion in range(n):
    
    for digito in range(10):
        intentos += 1
        
        if str(digito) == clave[posicion]:
            prefijo += str(digito)
            break  

print(f"Clave encontrada: {prefijo}")
print(f"Número de intentos:{intentos}")

"""
clave = input("Ingrese la clave: ")
n = len(clave)

intentos = 0
menor = 0
mayor= (10**n)-1

while menor <= mayor:
    intentos += 1

    mitad = (menor + mayor) // 2

    if str(mitad).zfill(n) == clave:
        print("encontrada")
        print(f"numero intentos : {intentos}")
        break
    elif mitad <  int(clave):
        menor = mitad + 1
    else:
        mayor = mitad -1


"""