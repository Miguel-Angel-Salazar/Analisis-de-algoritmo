def palindromo(texto):
    for i in range(len(texto)):
        for j in range(len(texto)):
            if j == len(texto) - 1 - i:
                if texto[i] != texto[j]:
                    return False
    return True  




texto1 = "oso"
texto2 = "casa"
print(f"la palabra es palindomo:{palindromo(texto1)}")
print(f"la palabra es palindomo:{palindromo(texto2)}")


def palindromo(txt):
    texto_limpio = txt.replace(" ","").lower()
    izq = 0
    der = len(texto_limpio) -1

    while izq < der:
        if texto_limpio[izq] != texto_limpio[der]:
            return False
        izq += 1
        der -= 1
    return True

texto3 = "reconocer"
texto4 = "robar"
print(f"la palabra es palindomo:{palindromo(texto3)}")
print(f"la palabra es palindomo:{palindromo(texto4)}")


def pal_recursivo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    
    return pal_recursivo(palabra[1:-1])


texooo= "reconocer"
print(f"es palindromo: {pal_recursivo(texooo)}")

def pal_recursivo(palabra):
    n = len(palabra)
    def palabra_recursivo(iz, der):
        if iz >= der:
            return True
        if palabra[iz] != palabra[der]:
            return False
        return palabra_recursivo(iz +1, der -1) 
    return palabra_recursivo(0, n -1)

tex= "reconocer"
print(f"es palindromo: {pal_recursivo(tex)}")
    