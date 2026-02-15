# Dada una cadena, determinar si todos sus caracteres son únicos
# (no se repite ninguno). NO usar estructuras de datos adicionales.
#
# Ejemplo:
#   entrada: "abcdef"  → True
#   entrada: "abcaef"  → False (la 'a' se repite)

def caracteres_unicos(texto):
    for i in range(len(texto)):
        for j in range(i +1 , len(texto)):
            if texto[i] == texto[j]:
                return False
        return True
    

txt1 = "abcdef"
txt2 = "abcaef"
txt3 = "abcbbaef"
print(f"la entrada es: {caracteres_unicos(txt1)}")
print(f"la entrada es: {caracteres_unicos(txt2)}")
print(f"la entrada es: {caracteres_unicos(txt3)}")