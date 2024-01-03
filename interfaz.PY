#Importamos el archivo personaje en el que se ecuentra el código del juego
from EJERCICIO02 import personaje
#Definimos una función para la interfaz
def interfaz():
    print("       BIENVENIDO AL COMBATE       ")
    #Empieza el juego escogiendo su personaje cada jugador
    print(".Jugador 1 escoge tu personaje:")
    a = int(input(" 1. Guerrero \n 2. Mago \n 3. Soldado \n    "))
    if a == 1:
        jugador1 = personaje.guerrero
    elif a == 2:
        jugador1 = personaje.mago
    elif a == 3:
        jugador1 = personaje.soldado
    print("El jugador 1 escogió el personaje ", jugador1.get_nombre())
    #Muestra los atributos del personaje escogido
    jugador1.atributo()
    if a == 1:
        jugador1.cambiar_arma()
    print("-----------------------------")    
    print(".Jugador 2 escoge tu personaje:")
    b = int(input(" 1. Guerrero \n 2. Mago \n 3. Soldado \n    "))
    if b == 1:
        jugador2 = personaje.guerrero
    elif b == 2:
        jugador2 = personaje.mago
    elif b == 3:
        jugador2 = personaje.soldado
    print("El jugador 2 escogió el personaje ", jugador2.get_nombre())
    jugador2.atributo()
    if b == 1:
        jugador2.cambiar_arma()
    jugador2.atributo()
    print("-----------------------------")
    #Iniciamos el combante haciendo el llamado del método combate y definiendo los jugadores que pelearán
    print("     INICIO DEL COMBATE     ")
    personaje.combate(jugador1,jugador2)
#Llamamos a la función interfaz para poder observar en pantalla
interfaz()
