"""
Se te da un arreglo de enteros nums, donde estás inicialmente en el índice 0 y cada nums[i] indica la longitud máxima de salto que puedes realizar desde i. Determina si es posible llegar (o sobrepasar) el último índice del arreglo.

📥 Entrada
nums: arreglo de enteros no negativos.
📤 Salida
true si puedes llegar al último índice.
false en caso contrario.

Ejemplo 1 Entrada: nums = [2,3,1,1,4] Salida: true Explicación: desde 0 saltas a 1 (≤2), y desde 1 saltas 3 posiciones hasta el final.

Ejemplo 2 Entrada: nums = [3,2,1,0,4] Salida: false Explicación: inevitablemente quedas en 3, donde nums[3]=0 y no puedes avanzar.
"""
def puede_llegar_final(numeros):

    alcance_maximo = 0

    for indice in range(len(numeros)):

        # si llegamos a un punto al que no podemos acceder
        if indice > alcance_maximo:
            return False

        # actualizar el alcance máximo posible
        alcance_maximo = max(alcance_maximo, indice + numeros[indice])

    return True


numeros = [2,3,1,1,4]

print(puede_llegar_final(numeros))