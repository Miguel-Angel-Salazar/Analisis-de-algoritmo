def potencia(num,expo):
    if expo == 0:
        return 1
    mitad = potencia(num, expo //2)
    
    if expo % 2 == 0:
        return mitad * mitad
    else:
        return num * mitad * mitad

print(potencia(1,3))