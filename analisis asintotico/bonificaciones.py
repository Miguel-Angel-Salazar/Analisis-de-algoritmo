def encontrar_pareja(lista, objetivo):
    visitado = set()

    for valor in lista:
        if objetivo - valor in visitado:
            return True
        visitado.add(valor)
    return False

print("ejemplo")
lista = [100,50,300,220,10]
objetivo = 270

print(f"lista: {lista}, objetivo: {objetivo} -> los cuales son : {encontrar_pareja(lista,objetivo)} ")


lista = [100, 50, 300, 220, 10,  320, 500]

objetivo = int(input("Ingrese el numero objetivo:"))

for i in range(len(lista)):
  if i < len(lista):
    num1 = lista[i]
  for j in range(len(lista)):
    j += 1
    if j < len(lista):
      num2 = lista[j]

    if num1 + num2 == objetivo:
      print(f"Los numeros que suman {objetivo} son {num1} y {num2}")
      break