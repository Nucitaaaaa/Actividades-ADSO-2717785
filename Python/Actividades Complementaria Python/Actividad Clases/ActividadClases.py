
#Se define la Super clase / Clase padre
class Pokemon: 
    def __init__(self, nombre, vida, tipo, ataque): #Se define el Constructor (Para agregar objetos a la clase)
        # Se definen los Atributos:
        self.nombre = nombre 
        self.vida = vida
        self.tipo = tipo
        self.ataque = ataque

    #Se definen los metodos:
    def mostrarPokemon(self):
        print(f'Nombre: {self.nombre}\nTipo:{self.tipo}\nVida:{self.vida}\nAtaque:{self.ataque}')

#Se definen las Clases Hijas (Se especifica la herencia de la superclase en los ()) 

class Planta(Pokemon): #Clase hija
    def __init__(self, nombre, vida, tipo, ataque, ataquePlanta): #Se define el constructor 
        super().__init__(nombre, vida, tipo, ataque) #Atributos que se heredan la super clase
        self.ataquePlanta = ataquePlanta #Se agrega un atributo propio de la clase

    def mostrarPokemon(self):  #Metodo 
        super().mostrarPokemon() #Metodo que se hereda de la super clase
        print(f'Ataque Especial: {self.ataquePlanta}')

class Psiquico(Pokemon):  #Clase hija
    def __init__(self, nombre, vida, tipo, ataque, ataquePsiquico): #Se define el constructor 
        super().__init__( nombre, vida, tipo, ataque) #Se define la herencia de atributos de la super clase / clase padre
        self.ataquePsiquico = ataquePsiquico #Se agrega un atributo propio

    def mostrarPokemon(self): #Metodo 
        super().mostrarPokemon() #Metodo que se hereda de la super clase
        print(f'Ataque Especial: {self.ataquePsiquico}')

class Fuego(Pokemon):  #Clase hija
    def __init__(self, nombre, vida, tipo, ataque, ataqueFuego):  #Se define el constructor
        super().__init__( nombre, vida, tipo, ataque) #Se define la herencia de atributos de la super clase / clase padre
        self.ataqueFuego = ataqueFuego #Se agrega un atributo propio

    def mostrarPokemon(self): #Metodo
        super().mostrarPokemon() #Metodo que se hereda de la super clase
        print(f'Ataque Especial: {self.ataqueFuego}')

#Instancias de la clase
Pokes = [
        Pokemon('Ratatta', 5, 'Normal', 'Mordisco\n'), 
        Planta('Bulbasaur', 12, 'Planta', 'Placaje', 'Latigo Cepa\n'), 
        Psiquico('Golduck', 12, 'Psiquico', 'Anulación', 'Confusión\n'),
        Fuego('Rapidash', 12, 'Fuego', 'Placaje', 'Ascuas\n'),
        Planta('Ivysaur', 18, 'Planta', 'Placaje', 'Rayo Solar\n'),
        Fuego('Charizard', 25, 'Fuego', 'Garra Dragón', 'Lanzallamas\n'),
        Psiquico('Alakazam', 30, 'Psiquico', 'Psíquico', 'Bola Sombra\n'),
        Pokemon('Pidgey', 8, 'Normal', 'Ataque Rápido\n'),
        Planta('Venusaur', 36, 'Planta', 'Rayo Solar', 'Terremoto\n'),
        Fuego('Arcanine', 28, 'Fuego', 'Lanzallamas', 'Garra Ígnea\n'),
        Psiquico('Alakazam', 33, 'Psíquico', 'Psíquico', 'Rayo Confuso\n'),
        Pokemon('Eevee', 10, 'Normal','Mordisco\n'),
        Planta('Vileplume', 42, 'Planta', 'Drenadoras', 'Pétalo Venenoso\n'),
        Fuego('Magmar', 31, 'Fuego', 'Lanzallamas', 'Ascuas\n'),
        Psiquico('Hypno', 38, 'Psíquico', 'Confusión', 'Hipnosis\n'),
        Pokemon('Jigglypuff', 15, 'Normal', 'Canto\n')
]

#Llamado al metodo mostrar
for i in Pokes: #itera en las instancias de la lista
    i.mostrarPokemon()

        

        

    