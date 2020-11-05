# EJERCICIO 3) EL DECODIFICADOR

# Se tiene que realizar un juego con las siguientes instrucciones:

# 1. El programa decidirá 3 dígitos no repetidos. Ej: 123
# 2. El jugador deberá indicar 3 dígitos mediante la consola.
# 3. El programa nos devolverá una pista de las siguientes:
#
#     ¡Casi!: El jugador acertó los tres números, pero en el orden incorrecto.
#     Cerca: El jugador acertó un número en la posición correcta.
#     Nada: El jugador no acertó el resto de casos.
#
# 4. Basándonos en estas pruebas, el jugador tendrá que conseguir hacer que
#    coincidan los 3 dígitos en la misma posición, el programa responderá y
#    terminará con:
#                    ¡Enhorabuena, ahora eres un hacker!

# Por ejemplo, si intentamos jugar con la máquina y esta tiene almacenado el
# número 479, esto sería un ejemplo de una partida:

# >>> juego_decodificador()
# ¡Bienvenido al decodificador!
# ¿Cuál es tú apuesta?: 459
# Cerca, ¡sigue así!
# ¿Cuál es tú apuesta? 345
# Nada, inténtalo de nuevo.
# ¿Cuál es tú apuesta? 947
# ¡Casi!, reordénalos.
# ¿Cuál es tú apuesta? 479
# ¡Enhorabuena, ahora eres un hacker!
# >>>

# Es importante que el programa termine en esa sentencia.

# Notas:
# Hay que tener en cuenta la división de las tareas para completar este tiempo
# de tareas que podrían tener una complejidad elevada. ¡Divide y vencerás!
#
# Hay algunas instrucciones que pueden ser de utilidad para desarrollar este
# sencillo juego:

import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])
guess = input("¿Cuál es tú apuesta?: ")
print(guess)


numeros = []
digits = []
# 1 ***

# for i in range(0,3):
#   n = random.randint(0,9)
#  digits.append(n)

# print(digits)


import random

digits = []
numeros = []

#1

while len(digits) < 3:
    rnd = random.randint(0, 9)
    if rnd in digits:
        continue
    digits += [rnd]

print(digits)

def comparacion(numeros):

    primero = numeros[0]
    segundo = numeros[1]
    tercero = numeros[2]



    if numeros == digits:
        print("¡Enhorabuena, ahora eres un hacker!")
    elif (sorted(numeros) == sorted(digits)) and (numeros != digits):
        print("¡Casi!")
    elif primero in digits:
        print("Cerca")
    elif segundo in digits:
        print("Cerca")
    elif tercero in digits:
        print("Cerca")
    else:
        print("Nada")




def juego_decodificador(): 
    n = (input("¿Cuál es tú apuesta?: "))
    numeros = [int(x) for x in str(n)]
    print(numeros)
    comparacion(numeros)

    while(numeros != digits):
        numeros.clear()
        n = (input("¿Cuál es tú apuesta?: "))
        numeros = [int(x) for x in str(n)]
        print(numeros)
        comparacion(numeros)


juego_decodificador()