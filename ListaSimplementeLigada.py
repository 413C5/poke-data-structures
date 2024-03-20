class Nodo:
    def __init__(self,dato) -> None:
        self.dato=dato
        self.siguiente=None

class ListasSimplementeLigada(object):
    def __init__(self) -> None:
        self.primero=None
        self.ultimo=None
        self.tamaño=0


    def append(self,dato):
        nuevoNodo=Nodo(dato)
        if self.primero==None:
            self.primero=nuevoNodo
            self.ultimo=nuevoNodo
        else:
            self.ultimo.siguiente=nuevoNodo
            self.ultimo=nuevoNodo
        self.tamaño+=1

    def get(self,indice):
        if indice==self.tamaño-1:
            return self.ultimo
        elif indice==0:
            return self.primero
        elif not(indice <0 or indice >=self.tamaño):
            nodoActual=self.primero
            contador=0
            while contador!=indice:
                nodoActual=nodoActual.siguiente
                contador+=1
            return nodoActual
        else:
            return None

    def update(self,indice,dato):
        nodoObjetivo=self.get(indice)
        if nodoObjetivo!=dato:
            nodoObjetivo.dato=dato

    def __str__(self):
        nodoActual=self.primero
        l=[]
        while nodoActual !=None:
            l.append(nodoActual.dato)
            nodoActual=nodoActual.siguiente
        return str(l)

    #Obtener la longitud de la lista ligada
    def len(self):
        nodoActual=self.primero
        count=0
        while nodoActual !=None:
            count+=1
            nodoActual=nodoActual.siguiente
        return count

    #Insertar un elemento al inicio de la LSL/Listo
    def prepend(self,dato):
        nuevoNodo=Nodo(dato)
        if self.primero==None:
            self.primero=nuevoNodo
            self.ultimo=nuevoNodo
        else:
            nuevoNodo.siguiente=self.primero
            self.primero=nuevoNodo
        self.tamaño+=1

    #Sacar el primer elemento de la Lista Simple/Listo
    def shift(self):
        if self.tamaño!=0:
            nodoEliminado=self.primero
            self.primero=self.primero.siguiente
            nodoEliminado.siguiente=None
            self.tamaño-=1
            return nodoEliminado


    #Eliminar el último elemento de la Lista/Listo
    def pop(self):
        if self.tamaño == 0:
            print("No hay nodos en la lista")
        elif self.primero.siguiente == None:
            self.primero = None
            self.ultimo = None
            self.tamaño -=1
        else:
            nodoActual = self.primero
            for i in range(0,self.tamaño-2,1):
                nodoActual = nodoActual.siguiente
            nodoActual.siguiente = None
            self.ultimo = nodoActual
            self.tamaño -=1
        
    
    #Insertar un elemento en cualquier posicion
    def insert(self,indice,dato):
        if indice==self.tamaño:
            self.append(dato)
        elif not(indice <0 or indice >=self.tamaño):
            nuevoNodo=Nodo(dato)
            nodoActual=self.get(indice)
            nuevoNodo.siguiente=nodoActual.siguiente
            nodoActual.siguiente=nuevoNodo
            self.tamaño+=1
        else:
            return None

    def remove(self,indice):
        if indice==0:
            return self.shift()
        elif indice==self.tamaño-1:
            return self.pop()
        elif indice>0 and indice<self.tamaño:
            nodoAnterior=self.get(indice-1)
            nodoEliminado=nodoAnterior.siguiente
            nodoAnterior.siguiente=nodoEliminado.siguiente
            nodoEliminado.siguiente=None
            self.tamaño-=1
            return nodoEliminado
        else:
            return None

    def reverse(self):
        nodoAnterior=None               #Defino el nodoAnterior
        nodoActual=self.primero         #Defino el nodo actual que va a ser el primero
        while nodoActual!=None:         #Porque una vez que nodoActual sea None quiere decir que ya se termino de hacer reversa, puntero es None
            nodoSiguiente=nodoActual.siguiente
            nodoActual.siguiente=nodoAnterior
            nodoAnterior=nodoActual
            nodoActual=nodoSiguiente
        self.primero=nodoAnterior
    
    def checar(self,dato):
        c = False
        nodoActual = self.primero
        while nodoActual != None:
            if nodoActual.dato == dato:
                c = True
            nodoActual = nodoActual.siguiente
        return c

        
        


