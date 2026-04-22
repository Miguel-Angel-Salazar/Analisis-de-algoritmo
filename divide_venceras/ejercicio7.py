def es_palindromo_indices(palabra, inicio=0, fin=None):
    if fin is None:
        fin = len(palabra) - 1

    if inicio >= fin:
        return True
    
    if palabra[inicio] != palabra[fin]:
        return False
    
    return es_palindromo_indices(palabra, inicio + 1, fin - 1)

print(es_palindromo_indices("reconocer"))  
print(es_palindromo_indices("python")) 


#______________________________________

def es_palindromo_mitad(palabra):
    
    if len(palabra) <= 1:
        return True
    
    mitad = len(palabra) // 2
    
    izquierda = palabra[:mitad]
    derecha = palabra[-mitad:]
    
    return izquierda == derecha[::-1]

print(es_palindromo_mitad("amolapaloma"))