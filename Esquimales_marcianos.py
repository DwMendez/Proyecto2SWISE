"Juego: Esquimales marcianos"

import random
import os

"Crear matriz a modo de tablero de juego"
def Crear_tablero(filas, columnas, valor):

    tablero = []
    for i in range(filas):
        tablero.append([])
        for j in range(columnas):
            tablero[i].append(valor)
    return tablero

"Mostrar en pantalla"
def Mostrar_tablero(tablero):

    for fila in tablero:
        for elemento in fila:
            print(elemento, end= " ")
        print()

#Parametros del juego#

bateria = 150
bloque = False #Se planea que se convierta en un objeto
columnas = 16
filas = 12

visible = Crear_tablero(filas, columnas, "-")

oculto = Crear_tablero(filas, columnas, 0)

"Distribuir objetos ocultos en el tablero "
def Colocar_objeto (tablero, energia, filas, columnas):

    objetos_ocultos =[]
    numero = 0
    while numero < energia:
        y = random.randint(0, filas-1)
        x = random.randint(0, columnas-1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            numero += 1
            objetos_ocultos.append((y,x))
    return tablero, objetos_ocultos


"Pantalla de presentación"
def presentacion():

    os.system("cls")

    print("***********************************************************")
    print("*                                                         *")
    print("*                  Esquimales Marcianos                   *")
    print("*                                                         *")
    print("*                  w/a/s/d para moverse                   *")
    print("*                                                         *")
    print("* Con r puedes crear bloques de hielo extraidos del suelo *")
    print("*                                                         *")
    print("*      Si te quedas sin baterias se termina el juego      *")
    print("*                                                         *")
    print("*          Crea estructuras como las siguientes:          *")
    print("*                                                         *")
    print("*                       ###    # # #                      *")
    print("*                      #####   #####                      *")
    print("*                      ## ##   ## ##                      *")
    print("*                                                         *")
    print("***********************************************************")
    print()
    input(" 'Enter' para empezar ... ")

"Devuelve el movimiento u opción elegida por el usuario"
def menu():

    print()
    print("Batería: ", bateria)

    if bloque == (False):
        print("No sostienes ningun bloque, presione r para extraer o mover un bloque del suelo")
    else:
        print("Sostienes un bloque, puedes presione r para soltarlo en el suelo")

    opcion = input("Use w/s/a/d para moverse: ")

    return opcion

columnas = 16
filas = 12

visible = Crear_tablero(filas, columnas, "-")

oculto = Crear_tablero(filas, columnas, 0)

oculto, objetos_ocultos = Colocar_objeto(oculto, 15, filas, columnas)

presentacion ()


# Colocamos jugador en el tablero
# Realmente no hay gran necesidad de usar randdm, pero asi nos genera una posición aleatoria que con más desarrollo podría cobrar sentido

y = random.randint(2, filas-3)
x = random.randint(2, columnas-3)

real = visible [y][x]
visible [y][x] = "☺"

os.system("cls")

Mostrar_tablero(visible)

# Bucle principal

suelo = []

jugando = True

while jugando:

    mov = menu()

    if mov == "w":
        if y == 0:
            y = 0
        else:
            visible [y][x] = real
            y -= 1
            real = visible[y][x]
            visible[y][x] = "☺"

    elif mov == "s":
        if y == filas-1:
            y = filas-1
        else:
            visible [y][x] = real
            y += 1
            real = visible [y][x]
            visible[y][x] = "☺"

    elif mov == "a":
        if x == 0:
            x = 0
        else:
            visible [y][x] = real
            x -= 1
            real = visible [y][x]
            visible[y][x] = "☺"

    elif mov == "d":
        if x == columnas-1:
            x = columnas-1
        else:
            visible [y][x] = real
            x += 1
            real = visible [y][x]
            visible[y][x] = "☺"

    elif mov == "r":
        if real == "-"  and bloque == (False) and oculto [y][x] == 0:
            visible [y][x] = "■"
            real = visible [y][x]
            bloque = (True)
            if (y,x) in suelo:
                suelo.remove((y,x))

        elif real == "-"  and bloque == (False) and oculto [y][x] == 9:
            visible [y][x] = "E"
            print("")
            print("")
            print("¡En hora buena, has encontrado una fuente de gas natural!")
            print("Se colocara una E en el mapa para que puedas recargar tu bateria")
            print("Presiona r cuando no estes cargando un bloque para cargar 20 puntos")
            real = visible [y][x]
            if (y,x) in suelo:
                suelo.remove((y,x))


        elif real == "E" and bloque == (False):
            bateria += 21

        elif real == "-" and bloque == (True):
            visible [y][x] = "□"
            real = visible [y][x]
            bloque = (False)
            if (y,x) in suelo:
                suelo.remove((y,x))

        elif real == "■" and bloque == (True):
            visible [y][x] = "-"
            real = visible [y][x]
            bloque = (False)
            if (y,x) in suelo:
                suelo.remove((y,x))

        elif real == "□" and bloque == (False):
            visible [y][x] = "-"
            real = visible [y][x]
            bloque = (True)
            if (y,x) in suelo:
                suelo.remove((y,x))

    bateria -=1
    if bateria == 0:
        jugando = False

    os.system("cls")

    Mostrar_tablero(visible)