def max_min(arr):
    maximo = minimo = arr[0]

    for valor in arr[1:]:
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor
    return maximo, minimo


#__________________________________________

def max_min_dv(arr,inicio,final):

    if inicio== final:
        return arr[inicio], arr[inicio]

    if final == inicio + 1:
        if arr[inicio] > arr[final]:
            return arr[inicio], arr[final]
        else:
            return arr[final], arr[inicio]

    medio = (inicio + final) // 2

    max1, min1 = max_min_dv(arr, inicio, medio)
    max2, min2 = max_min_dv(arr, medio + 1, final)

    return max(max1, max2), min(min1, min2)

arr = [3, 8, 2, 5, 1, 9]
maximo, minimo = max_min_dv(arr, 0, len(arr)-1)
print(maximo, minimo)