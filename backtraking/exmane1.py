"""
1) Cómo reconocer un problema de Backtracking en 10 segundos

Si el problema tiene estas características, casi seguro es backtracking:

Señales claras:
Hay que probar posibilidades.
La solución se construye paso a paso.
En cada paso hay varias opciones.
Algunas decisiones pueden hacer que la solución sea inválida.
Quieren:
todas las soluciones,
una solución válida,
o la mejor solución entre muchas.
Frase mental:

“Voy armando una solución parcial, y si veo que ya no sirve, me devuelvo.”

Eso es backtracking.
2) formato general de un algoritmo de Backtracking
def backtrack(estado_actual):
    if caso_base:
        guardar_respuesta()
        return

    for opcion in opciones_posibles:
        if es_valida(opcion):
            hacer(opcion)
            backtrack(nuevo_estado)
            deshacer(opcion)
3) Lo MÁS importante del examen: ¿cómo encontrar la PODA?

Esta es la parte clave.

Regla de oro:

La poda aparece cuando puedes decir:

“Aunque siga explorando por aquí, ya sé que esto no puede terminar bien”.

Entonces cortas esa rama.

4) Tipos de poda que más salen en examen
PODA TIPO 1: Restricción violada

La más fácil y más común.

Idea:

Si la solución parcial ya incumple una regla, no tiene sentido seguir.

Ejemplo:
“La suma no puede pasar de 10”
“No se pueden repetir números”
“No pueden ir dos personas incompatibles juntas”
“No puede haber dos letras iguales consecutivas”
Forma mental:

“Ya me pasé / ya rompí una regla / ya quedó inválido”.

✅ Se poda inmediatamente.

PODA TIPO 2: Ya no alcanza para completar

Muy típica y muy buena.

Idea:

Aunque sigas, ya no te quedan suficientes elementos para completar la solución.

Ejemplo:

“Debo escoger 4 elementos y llevo 2, pero solo me queda 1 disponible”.

Entonces:

necesito 2 más,
pero solo hay 1,
imposible terminar.
Condición típica:
if len(solucion_actual) + elementos_restantes < tamaño_objetivo:
    return
Forma mental:

“Ya no me da”.

PODA TIPO 3: Me pasé del objetivo

Muy común en problemas de suma, peso, costo, capacidad, etc.

Ejemplo:
suma objetivo = 15
llevas 18

Ya no sirve seguir si solo puedes agregar positivos.

Condición típica:
if suma_actual > objetivo:
    return
Forma mental:

“Ya me pasé, no hay forma de arreglarlo”.

⚠️ Ojo: esta poda solo sirve si no existen negativos o algo que pueda compensar.

PODA TIPO 4: No puede superar la mejor solución actual

Esto sale cuando el problema es de optimización:

máximo valor,
mínimo costo,
mejor combinación,
etc.
Idea:

Si ya tienes una mejor respuesta guardada, y esta rama ni en el mejor caso puede superarla, la cortas.

Ejemplo:

“Quiero el subconjunto de mayor suma sin pasarme de 20”.

Si una rama actual lleva suma 7, y aun usando todo lo que queda solo llegaría a 10, pero ya tienes una solución de 14…

❌ Esa rama ya no sirve.

Forma mental:

“Ni esforzándose esta rama gana”.

Esto ya es una poda más fuerte.

5) Cómo sacar la poda en un examen paso a paso

Cuando leas el enunciado, pregúntate esto:

Pregunta 1:
“¿Qué hace inválida una solución parcial?”

Eso te da la poda más obvia.

Ejemplos:

repetir elementos,
exceder una suma,
romper una regla de adyacencia,
usar más recursos de los permitidos.
Pregunta 2:
“¿Qué me falta para completar la solución?”

Eso te da la poda de “ya no alcanza”.

Ejemplos:

faltan k elementos,
faltan letras,
faltan grupos,
faltan posiciones.
Pregunta 3:
“¿Hay una meta numérica que pueda pasarme?”

Eso te da poda por exceso.

Ejemplos:

suma,
costo,
peso,
tiempo,
capacidad.
Pregunta 4:
“¿Estoy buscando la mejor solución?”

Eso te da poda por comparación con la mejor actual.

6) La plantilla mental que debes decir en el examen

Cuando te pidan explicar la poda, puedes escribir algo como esto:

Criterio de poda:
Se detiene la exploración de una rama cuando la solución parcial ya no puede conducir a una solución válida u óptima.
En este caso, se poda cuando ________, porque continuar explorando no produciría una respuesta útil.

Y luego lo adaptas:

“...cuando la suma parcial supera el objetivo”
“...cuando se repite un elemento”
“...cuando no quedan suficientes elementos para completar la solución”
“...cuando la rama actual no puede superar la mejor solución encontrada”

Eso queda muy bien explicado.

"""