#Pokemon
class Pokemon:
    #Constructor
    def __init__(self) -> None:
        self.numero=None
        self.nombre=None
        self.tipo1=None
        self.tipo2=None
        self.habilidad=None
        self.generacion = None
        self.region = None

    #Nombre
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    #Tipos
    def getTipo1(self):
        return self.tipo1
    
    def setTipo1(self,tipo1):
        self.tipo1=tipo1

    def getTipo2(self):
        return self.tipo2
    
    def setTipo2(self,tipo2):
        self.tipo2=tipo2

    #Numero Pokedex
    def getNumero(self):
        return self.numero
    
    def setNumero(self,numero):
        self.numero=numero

    #Habilidad
    def getHabilidad(self):
        return self.habilidad

    def setHabilidad(self,habilidad):
        self.habilidad=habilidad

    #Generacion
    def getGeneracion(self):
        return self.generacion
    def setGeneracion(self,generacion):
        self.generacion = generacion

    #Region
    def getRegion(self):
        return self.region
    def setRegion(self,region):
        self.region = region


class Region:
    #Constructor
    def __init__(self) -> None:
        self.nombre=None
        self.año=None
    
    #Año en el que se introdujo la región
    def getAño(self):
        return self.año
    
    def setAño(self,año):
        self.año=año
    
    #Nombre
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

class Generacion:
    #Constructor
    def __init__(self) -> None:
        self.nombre=None
        self.consola=None

    #Nombre generación (Se maneja con numeros romanos)
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre=nombre

    #Consola
    def getConsola(self):
        return self.consola

    def setConsola(self,consola):
        self.consola=consola

class Id:
    #Constructor
    def __init__(self) -> None:
        self.numero=None
        self.juego=None

    #Numero
    def getNumero(self):
        return self.numero
    
    def setNumero(self,contador):
        self.numero=contador

    #Juego
    def getJuego(self):
        return self.juego

    def setJuego(self,juego):
        self.juego=juego

class Pokedex:
    def __init__(self) -> None:
        self.id=None
        self.nombre=None
        self.pokemones = None
        self.generacion = None
        self.region = None
    
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setPokemones(self,lista):
        self.pokemones = lista
    def getPokemones(self):
        return self.pokemones
    def appendPokemones(self,dato,pokemon):
        self.pokemones.insert(dato,pokemon)

    def setGeneracion(self,generacion):
        self.generacion = generacion

    def getGeneracion(self):
        return self.generacion

    def setRegion(self,region):
        self.region = region

    def getRegion(self):
        return self.region