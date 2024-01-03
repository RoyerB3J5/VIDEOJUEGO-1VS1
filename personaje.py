#Clase padre
class personaje:
    # Realizamos la abstracción, al definir los atributos en el método constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
# Los atributos están definidos de manera pública (ENCAPSULAMIENTO)
    def atributo(self):
        print(self.nombre, ":", sep =" ")
        print(".Fuerza:", self.fuerza)
        print(".Inteligenica:", self.inteligencia)
        print(".Defensa:", self.defensa)
        print(".Vida:", self.vida)

#Definimos los métodos que se podrán usar en combate
    def subir_nivel(self,fuerza, inteligencia,defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida>0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, " ha muerto")
    
    def daño(self,enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, " puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, " es ", enemigo.vida)
        else:
            enemigo.morir()
            
    
#Utilizamos herencia, al uzar métodos de la clase padre (personaje) en las clases hija (guerrero)
class Guerrero(personaje):
    
    def __init__(self, nombre,fuerza, inteligencia,defensa,vida,arma):
        super().__init__(nombre,fuerza, inteligencia,defensa, vida)
        self.arma = arma
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma : \n (1) Espada, daño 4.\n (2) Acha, daño 6.\n "))
        if opcion == 1 :
            self.arma = 2
        elif opcion == 2:
            self.arma = 4
        else :
            print("Numero de arma incorrecto")

    def atributo(self):
        super().atributo()
        print(".Arma : ", self.arma)
    
    def daño(self, enemigo):
        return self.fuerza*self.arma - enemigo.defensa
    
#Utilizamos herencia, al uzar métodos de la clase padre (personaje) en las clases hija (MAGO)
class Mago(personaje):

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida,libro):
        super().__init__(nombre,fuerza,inteligencia,defensa,vida)
        self.libro = libro

    def atributo(self):
        super().atributo()
        print(".Libro: ", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
soldado = personaje("Soldado",15,8,10,100)
guerrero = Guerrero("Guerrero",10,10,4,100,4)
mago = Mago("Mago",5,8,4,100,3)

#Utilizamos el polimorfismo, al calcular el daño dará valores diferentes dependiendo el tipo de personaje que se escoja
#Existen varias formas de atacar dependiendo del personaje
def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>>Accion de ", jugador_1.get_nombre(), " : ", sep = " " )
        #Declaramos el método atacar para que empiece el combate
        jugador_1.atacar(jugador_2)
        if jugador_2.vida == 0 :
            break
        print(">>>Accion de ", jugador_2.get_nombre(), " : ", sep = " " )
        jugador_2.atacar(jugador_1)
        if jugador_1.vida == 0 :
            break
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado ", jugador_1.get_nombre())
    elif jugador_2.esta_vivo():
        print("\nHa ganado ", jugador_2.get_nombre())
    else:
        print("\nEmpate")


