def f1(matrix, x):
  
  for fila in  range(len(matrix)):
    for columna in range(len(matrix[fila])):
      if matrix[fila][columna] == x:
        return True
  return False


max1 = [
  [3,5,2],
  [7,1,9],
  [4,6,8]
  
]        


print(f"el valor de x fue encontrado:{f1(max1,1)}")