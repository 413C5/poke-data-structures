class Nodo:
    def __init__(self, dato,objeto) -> None:
        self.objeto=objeto
        self.dato=dato
        self.hijoIzquierdo=None
        self.hijoDerecho=None


class ArbolBusquedaBinaria:
    def __init__(self) -> None:
        self.raiz=None
    

    def insert(self, dato,objeto):
        nuevoNodo=Nodo(dato,objeto)
        if self.raiz==None:
            self.raiz=nuevoNodo
        else:
            def recorrer(dato,nodoActual):
                if dato==nodoActual.dato:
                    return False
                elif dato<nodoActual.dato:
                    if nodoActual.hijoIzquierdo==None:
                        nodoActual.hijoIzquierdo=nuevoNodo
                        return True
                    else:
                        return recorrer(dato,nodoActual.hijoIzquierdo)
                    
                elif dato>nodoActual.dato:
                    if nodoActual.hijoDerecho==None:
                        nodoActual.hijoDerecho=nuevoNodo
                        return True
                    else:
                        return recorrer(dato,nodoActual.hijoDerecho)

            return recorrer(dato,self.raiz)
    

    def find(self,dato):#Funciona
        def recorrer(dato,nodoActual):
            if dato==nodoActual.dato:
                return nodoActual
                
            elif dato<nodoActual.dato:
                if nodoActual.hijoIzquierdo==None:
                    return None
                else:
                    return recorrer(dato,nodoActual.hijoIzquierdo)
                    
            elif dato>nodoActual.dato:
                if nodoActual.hijoDerecho==None:
                    return None
                else:
                    return recorrer(dato,nodoActual.hijoDerecho)
        if self.raiz != None:
            return recorrer(dato,self.raiz)
        else:
            return None

    def delete(self,dato):
        nodoUsado = self.find(dato)
        if nodoUsado != None:
            def recorrerMenor(nodoActual, nodoMenor = None): #Funcion que busca el nodo menor
                if nodoActual.dato < nodoMenor.dato: #Si el nodo actual es menor que el menor se cambian datos
                    nodoMenor = nodoActual
                if nodoActual.hijoIzquierdo != None: #Se aplica recursivamente a los hijos del nodo padre si tiene
                    nodoMenor = recorrerMenor(nodoActual.hijoIzquierdo,nodoMenor)
                if nodoActual.hijoDerecho != None:
                    nodoMenor = recorrerMenor(nodoActual.hijoDerecho,nodoMenor)
                return nodoMenor #Se devuelve el nodo menor

            def recorrerBusquedaP(nodoActual = None, nodoMenor = None,nodoPadre = self.raiz): #Funcion que busca padres
                if nodoActual == nodoMenor: #Si el nodo actual es igual a menor se cambian datos
                    nodoMenor = nodoActual
                else:
                    if nodoActual.hijoIzquierdo != None: #Se aplica recursivamente a los hijos del nodo padre si tiene
                        nodoPadre,nodoMenor = recorrerBusquedaP(nodoActual.hijoIzquierdo,nodoMenor,nodoPadre)
                        if nodoMenor == nodoActual.hijoIzquierdo:
                            nodoPadre = nodoActual
                    if nodoActual.hijoDerecho != None:
                        nodoPadre,nodoMenor = recorrerBusquedaP(nodoActual.hijoDerecho,nodoMenor,nodoPadre)
                        if nodoMenor == nodoActual.hijoDerecho:
                            nodoPadre = nodoActual
                return nodoPadre,nodoMenor #Se devuelve el nodo padre               

            def recorrerBorrar(nodoActual,Padre): #Funcion para borrar nodos
                if nodoActual.hijoDerecho == None and nodoActual.hijoIzquierdo == None: #Borra si es una hoja
                    if self.raiz == nodoActual: #Si el nodo actual es la raíz solo se borra y ya
                        self.raiz = None
                    elif Padre.hijoIzquierdo == nodoActual: #Se quita su enlace con el padre en cualquier caso de hoja
                        Padre.hijoIzquierdo = None
                    elif Padre.hijoDerecho == nodoActual:
                        Padre.hijoDerecho = None
                elif nodoActual.hijoIzquierdo != None and nodoActual.hijoDerecho == None: #Borra el nodo y se reemplaza con uno de sus hijos
                    nodoActual.dato,nodoActual.objeto = nodoActual.hijoIzquierdo.dato,nodoActual.hijoIzquierdo.objeto
                    recorrerBorrar(nodoActual.hijoIzquierdo,nodoActual)
                elif nodoActual.hijoDerecho != None and nodoActual.hijoIzquierdo == None: #Se borra el nodo y se reemplaza con el hijo de menor tamaño del lado derecho
                    nodoActual.dato,nodoActual.objeto = nodoActual.hijoDerecho.dato,nodoActual.hijoDerecho.objeto
                    recorrerBorrar(nodoActual.hijoDerecho,nodoActual)
                else:
                    nodoMenor = recorrerMenor(nodoActual.hijoDerecho,nodoActual.hijoDerecho) #Encontramos el nodo menor al lado derecho
                    Padre2,nodoBasura = recorrerBusquedaP(self.raiz,nodoMenor) #Encontramos el nodo padre de ese nodo
                    nodoActual.dato,nodoActual.objeto = nodoMenor.dato,nodoMenor.objeto #Se reemplazan los datos del nodo actual con el nodo menor
                    recorrerBorrar(nodoMenor,Padre2) #Se borra el nodo menor

            Padre,nodoBasura = recorrerBusquedaP(self.raiz,nodoUsado)
            recorrerBorrar(nodoUsado,Padre)
            return True
        else:
            return False
    

    #Recorridos en el arbol
    def preorden(self):
        notacionPrefija=[]

        def recorrer(nodoActual):
            notacionPrefija.append(nodoActual)
            if nodoActual.hijoIzquierdo!=None:
                recorrer(nodoActual.hijoIzquierdo)
            if nodoActual.hijoDerecho!=None:
                recorrer(nodoActual.hijoDerecho)
        if self.raiz != None:
            recorrer(self.raiz)
        return notacionPrefija

    def inorden(self):
        notacionInfija=[]

        def recorrer(nodoActual):
            if nodoActual.hijoIzquierdo!=None:
                recorrer(nodoActual.hijoIzquierdo)
            notacionInfija.append(nodoActual)
            if nodoActual.hijoDerecho!=None:
                recorrer(nodoActual.hijoDerecho)
        if self.raiz != None:
            recorrer(self.raiz)
        return notacionInfija

    
    def posorden(self):
        notacionPosfija=[]

        def recorrer(nodoActual):
            if nodoActual.hijoIzquierdo!=None:
                recorrer(nodoActual.hijoIzquierdo)
            if nodoActual.hijoDerecho!=None:
                recorrer(nodoActual.hijoDerecho)
            notacionPosfija.append(nodoActual)
        if self.raiz != None:
            recorrer(self.raiz)
        return notacionPosfija
