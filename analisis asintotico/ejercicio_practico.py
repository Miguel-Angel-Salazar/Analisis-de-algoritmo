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

contraseña = input("Ingrese su contraseña")
n = len(contraseña)
intentos = 0

for i in range(0,n):
    clave_generada = str(i).zfill(n) 
    intentos += 1

    if clave_generada == contraseña:
        print("el candado abre")
        print(f"la clave es {clave_generada} y se intentó {intentos} veces")
        break



contraseña = input("Ingrese su contraseña")
n = len(contraseña)
intentos = 0

while clave_generada != contraseña:
        clave_generada = str(i).zfill(n) 
        intentos += 1
        i += 1

if clave_generada == contraseña:
    print("el candado abre")
    print(f"la clave es {clave_generada} y se intentó {intentos} veces")
            break

