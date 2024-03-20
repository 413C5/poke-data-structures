from tkinter import *
from ListaSimplementeLigada import ListasSimplementeLigada
import os
from clases import Pokemon,Region,Generacion,Id,Pokedex
from Arbol import ArbolBusquedaBinaria
os.system('cls')

#Listas de base de datos
pokedex=ListasSimplementeLigada()
region=ListasSimplementeLigada()
generacion=ListasSimplementeLigada()
id=ListasSimplementeLigada()


#Para realizar la busqueda
arbolPokemon=ArbolBusquedaBinaria()
arbolId=ArbolBusquedaBinaria()
arbolPokedex = ArbolBusquedaBinaria()


#En donde finalmente almaceno todo
lsl=ListasSimplementeLigada()

'''
p=Region()
p.setNombre('Kanto')
p.setAño(2000)
region.append(p)
p=Region()
p.setNombre('Johto')
p.setAño(2000)
region.append(p)
p=Region()
p.setNombre('Hoenn')
p.setAño(2000)
region.append(p)

print(region)

p=Generacion()
p.setNombre('I')
p.setConsola('GB')
generacion.append(p)
p=Generacion()
p.setNombre('II')
p.setConsola('GB')
generacion.append(p)
p=Generacion()
p.setNombre('III')
p.setConsola('GB')
generacion.append(p)

print(generacion)

p=Pokemon()
p.setNumero(int(1))
p.setNombre('Pikachu')

arbolPokemon.insert(p.getNumero(),p)
'''

def seleccionar():
    #print('Opcion1:',opcion1.get())
    #print('Opcion2:',opcion2.get())

    if opcion2.get()==1:
        limpiar()
        colocar(opcion1.get(),opcion2.get())
        #gregar() 

    elif opcion2.get()==2:
        limpiar()
        colocar(opcion1.get(),opcion2.get())
        #baja(opcion1.get()) 

    elif opcion2.get()==3:
        limpiar()
        colocar(opcion1.get(),opcion2.get())
        #consultar(opcion1.get())

    elif opcion2.get()==4:
        limpiar()
        colocar(opcion1.get(),opcion2.get())
        #modificar(opcion1.get()) 

    if opcion2.get()==5:
        limpiar()
        colocar(opcion1.get(),opcion2.get())
        #reporte(opcion1.get())

def limpiar():
    etiqueta1.place_forget()
    etiqueta2.place_forget()
    etiqueta3.place_forget()
    etiqueta4.place_forget()
    etiqueta5.place_forget()
    etiqueta6.place_forget()
    etiqueta7.place_forget()
    etiqueta8.place_forget()

    caja1.place_forget()
    caja2.place_forget()
    caja3.place_forget()
    caja4.place_forget()
    caja5.place_forget()
    caja6.place_forget()
    caja7.place_forget()

    boton2.place_forget()
    boton3.place_forget()
    boton4.place_forget()
    boton5.place_forget()
    boton6.place_forget()

def colocar(opc1,opc2):
    print('Valor Opcion1:',opcion1.get())
    print('Valor Opcion2:',opcion2.get())
    #Agregar
    if opc2==1:
        #Pokemon
#Etiquetas #listo
        #
        if opc1==1:
            etiqueta1.config(text="Numero:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Nombre:")
            etiqueta2.place(x=180,y=490)
            etiqueta3.config(text="Tipo 1:")
            etiqueta3.place(x=180,y=530)
            etiqueta4.config(text="Tipo 2:")
            etiqueta4.place(x=180,y=570)
            etiqueta5.config(text="Habilidad:")
            etiqueta5.place(x=180,y=610)
            etiqueta6.config(text="Generacion:")
            etiqueta6.place(x=180,y=650)
            etiqueta7.config(text="Region:")
            etiqueta7.place(x=180,y=690)
            #Dummy
            etiqueta8.config(text="")
            etiqueta8.place(x=180,y=730)

            caja1.place(x=355,y=450)
            caja2.place(x=355,y=490)
            caja3.place(x=355,y=530)
            caja4.place(x=355,y=570)
            caja5.place(x=355,y=610)
            caja6.place(x=355,y=650)
            caja7.place(x=355,y=690)

            boton2.place(x=550,y=440)
            
        #Region
        elif opc1==2:
            etiqueta1.config(text="Nombre:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Año:")
            etiqueta2.place(x=180,y=490)

            caja2.place(x=355,y=450)
            caja1.place(x=355,y=490)

            boton2.place(x=550,y=440)

        #Generacion
        elif opc1==3:
            etiqueta1.config(text="Nombre:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Consola:")
            etiqueta2.place(x=180,y=490)

            caja2.place(x=355,y=450)
            caja3.place(x=355,y=490)

            boton2.place(x=550,y=440)

        #Id
        elif opc1==4:
            etiqueta1.config(text="Numero:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Juego:")
            etiqueta2.place(x=180,y=490)

            caja1.place(x=355,y=450)
            caja2.place(x=355,y=490)

            boton2.place(x=550,y=440)

        #Pokedex
        elif opc1==5:
            boton2.place(x=550,y=440)

    #Dar de baja
    elif opc2==2:
        #Pokemon
        if opc1==1:
            etiqueta1.config(text="Numero pokemon:")
            etiqueta1.place(x=180,y=450)

            caja1.place(x=355,y=450)

            boton3.place(x=550,y=440)
        
        #Region
        elif opc1==2:
            etiqueta1.config(text="Nombre region:")
            etiqueta1.place(x=180,y=450)

            caja2.place(x=355,y=450)

            boton3.place(x=550,y=440)

        #Generacion
        elif opc1==3:
            etiqueta1.config(text="Nombre generacion:")
            etiqueta1.place(x=180,y=450)

            caja2.place(x=355,y=450)

            boton3.place(x=550,y=440)


        #Id
        elif opc1==4:
            etiqueta1.config(text="Numero id:")
            etiqueta1.place(x=180,y=450)

            caja1.place(x=355,y=450)

            boton3.place(x=550,y=440)

        #Pokedex
        elif opc1==5:
            boton3.place(x=550,y=440)

    #Consultar
    elif opc2==3:
        #Pokemon
        if opc1==1:
            etiqueta1.config(text="Numero pokemon:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Nombre:")
            etiqueta2.place(x=180,y=490)
            etiqueta3.config(text="Tipo 1:")
            etiqueta3.place(x=180,y=530)
            etiqueta4.config(text="Tipo 2:")
            etiqueta4.place(x=180,y=570)
            etiqueta5.config(text="Habilidad:")
            etiqueta5.place(x=180,y=610)
            etiqueta6.config(text="Generacion:")
            etiqueta6.place(x=180,y=650)
            etiqueta7.config(text="Region:")
            etiqueta7.place(x=180,y=690)

            caja1.place(x=355,y=450)

            boton4.place(x=550,y=440)
        
        #Region
        elif opc1==2:
            etiqueta1.config(text="Nombre de la region:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Año introducida:")
            etiqueta2.place(x=180,y=490)

            caja2.place(x=355,y=450)

            boton4.place(x=550,y=440)
            

        #Generacion
        elif opc1==3:
            etiqueta1.config(text="Nombre de la generacion:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Consola:")
            etiqueta2.place(x=180,y=490)

            caja2.place(x=355,y=450)

            boton4.place(x=550,y=440)


        #Id
        elif opc1==4:
            etiqueta1.config(text="Numero de ID:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Juego:")
            etiqueta2.place(x=180,y=490)

            caja1.place(x=355,y=450)

            boton4.place(x=550,y=440)

        #Pokedex
        elif opc1==5:
            boton4.place(x=550,y=440)

    #Modificar
    elif opc2==4:
        #Pokemon
        if opc1==1:
            etiqueta1.config(text="Numero pokemon:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Nuevo nombre:")
            etiqueta2.place(x=180,y=490)
            etiqueta3.config(text="Nuevo tipo 1:")
            etiqueta3.place(x=180,y=530)
            etiqueta4.config(text="Nuevo tipo 2:")
            etiqueta4.place(x=180,y=570)
            etiqueta5.config(text="Nueva habilidad:")
            etiqueta5.place(x=180,y=610)
            etiqueta6.config(text="Nueva generacion:")
            etiqueta6.place(x=180,y=650)
            etiqueta7.config(text="Nueva region:")
            etiqueta7.place(x=180,y=690)

            caja1.place(x=355,y=450)
            caja2.place(x=355,y=490)
            caja3.place(x=355,y=530)
            caja4.place(x=355,y=570)
            caja5.place(x=355,y=610)
            caja6.place(x=355,y=650)
            caja7.place(x=355,y=690)

            boton5.place(x=550,y=440)
        
        #Region
        elif opc1==2:
            etiqueta1.config(text="Nombre de la region:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Nuevo nombre:")
            etiqueta2.place(x=180,y=490)
            etiqueta3.config(text="Nuevo año:")
            etiqueta3.place(x=180,y=530)

            caja2.place(x=355,y=450)
            caja3.place(x=355,y=490)
            caja1.place(x=355,y=530)

            boton5.place(x=550,y=440)
            

        #Generacion
        elif opc1==3:
            etiqueta1.config(text="Nombre de la generacion:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Nuevo nombre:")
            etiqueta2.place(x=180,y=490)
            etiqueta3.config(text="Nueva consola:")
            etiqueta3.place(x=180,y=530)

            caja2.place(x=355,y=450)
            caja3.place(x=355,y=490)
            caja4.place(x=355,y=530)

            boton5.place(x=550,y=440)


        #Id
        elif opc1==4:
            etiqueta1.config(text="Numero de ID:")
            etiqueta1.place(x=180,y=450)
            etiqueta2.config(text="Nuevo juego:")
            etiqueta2.place(x=180,y=490)

            caja1.place(x=355,y=450)
            caja2.place(x=355,y=490)

            boton5.place(x=550,y=440)

        #Pokdedex
        elif opc1==5:
            boton5.place(x=550,y=440)

    #Reporte
    elif opc2==5:
        #Tipos de recorrido
        #Pokemon
        if opc1==1:
            #dummy
            etiqueta1.config(text="")
            etiqueta1.place(x=180,y=450)

            boton6.place(x=550,y=440)
        
        #Region
        elif opc1==2:
            #dummy
            etiqueta1.config(text="")
            etiqueta1.place(x=180,y=450)
            
            boton6.place(x=550,y=440)
            

        #Generacion
        elif opc1==3:
            #dummy
            etiqueta1.config(text="")
            etiqueta1.place(x=180,y=450)

            boton6.place(x=550,y=440)


        #Id
        elif opc1==4:
            #dummy
            etiqueta1.config(text="")
            etiqueta1.place(x=180,y=450)

            boton6.place(x=550,y=440)

        elif opc1==5:
            boton6.place(x=550,y=440)
  

def agregar():
    #Pokemon
    if opcion1.get()==1:
        print('Valor',opcion1.get())
        print('agregar pokemon')
        print('Entro a agregar')
        varNum=False
        var=False
        var2=False
        p=Pokemon()
        p.setNumero(int(caja1.get()))
        if arbolPokemon.find(p.getNumero())!=None:
            print("El numero ya se encuentra registrado.Intente con otro:",end='')
            varNum=True
        p.setNombre(caja2.get())
        p.setTipo1(caja3.get())
        p.setTipo2(caja4.get())
        p.setHabilidad(caja5.get())
        p.setGeneracion(caja6.get())
        p.setRegion(caja7.get())
        

        #Se busca el nombre de la region en la lista
        for i in range(0,region.tamaño,1):
            print("%s %s" % (p.getRegion(),region.get(i).dato.getNombre()))
            if p.getRegion()==region.get(i).dato.getNombre():
                var=True
                break

        #Se busca la generacion en la lista
        for i in range(0,generacion.tamaño,1):
            print("%s %s" % (p.getGeneracion(),generacion.get(i).dato.getNombre()))
            if p.getGeneracion()==generacion.get(i).dato.getNombre():
                var2=True
                break

        #Si existen se agregan al objeto
        if var==True and var2==True and varNum==False:
            #Agrego datos al arbol para facilitar su busqueda
            arbolPokemon.insert(p.getNumero(),p)
            print('Se inserto en el arbol')
            etiqueta8.config(text='Pokemon agregado exitosamente')
            etiqueta8.place(x=300,y=290)
        
        #Caso contrario, no se agrega nada y se pierden los datos
        else:
            etiqueta8.config(text='ERROR:Generacion/Region/ID (ine)existente')
            etiqueta8.place(x=300,y=290)
            print('ERROR:Generacion/Region/ID (ine)existente')

    #Region
    elif opcion1.get()==2:
        print('Valor',opcion1.get())
        print('agregar region')

        var=True
        r=Region()
        r.setNombre(caja2.get())
        for i in range(0,region.tamaño,1):
            if r.getNombre()==region.get(i).dato.getNombre():
                var=False
                break

        if var==True:
            r.setAño(int(caja1.get()))
            region.append(r)
            print('Region agregada')
            etiqueta8.config(text='Region agregada exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='Nombre de region ya utilizado')
            etiqueta8.place(x=300,y=290)

    #Generacion
    elif opcion1.get()==3:
        print('Valor',opcion1.get())
        print('agregar generacion')

        var=True
        g=Generacion()
        g.setNombre(caja2.get())
        for i in range(0,generacion.tamaño,1):
            if g.getNombre()==generacion.get(i).dato.getNombre():
                var=False
                break

        if var==True:
            g.setConsola(caja3.get())
            generacion.append(g)
            print('Generacion agregada')
            etiqueta8.config(text='Generacion agregada exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='Nombre de generacion ya utilizado')
            etiqueta8.place(x=300,y=290)

    #Id
    elif opcion1.get()==4:
        print('Valor',opcion1.get())
        print('agregar id')
        var=False

        i=Id()
        #Con id ,numero es el unico valor que se checa su existencia en el arbol, pues ap
        i.setNumero(int(caja1.get()))
        i.setJuego(caja2.get())
        #Si existe la id
        if arbolId.find(i.getNumero())!=None:
            var=True

        if var==False:
            print('Id agregada')
            arbolId.insert(i.getNumero(),i)
            etiqueta8.config(text='Id agregada exitosamente')
            etiqueta8.place(x=300,y=300)

        else:
            etiqueta8.config(text='La Id ya existe.Por favor intente con otra')
            etiqueta8.place(x=300,y=290)
    
    elif opcion1.get()==5:
        os.system('cls')
        var = False
        pk = Pokedex()
        pk.setId(int(input("Numero de ID: ")))
        nodoObj = arbolId.find(pk.getId())
        if nodoObj != None: #Se checa que el id está en el árbol id
            if arbolPokedex.find(pk.getId()) == None: #Se checa que no esté repetido ya el id entre los pokedex
                pk.setNombre(arbolId.find(pk.getId()).objeto.getJuego())
                pk.setGeneracion(input("\nIntroduce la generacion a la que pertenece: ")) #Se añade la generacion
                for i in range(0,generacion.tamaño,1):
                    if pk.getGeneracion()==generacion.get(i).dato.getNombre():#Se checa si la generación existe
                        var=True
                        break
                if var == True:
                    var = False
                    pk.setRegion(input("\nIntroduce el nombre de la region: "))#Se añade la region
                    for i in range(0,region.tamaño,1):
                        if pk.getRegion()==region.get(i).dato.getNombre():#Se checa si la region existe
                            var=True
                            break
                    if var == True:
                        pk.setPokemones(ArbolBusquedaBinaria())#Se crea un objeto arbol binario de busqueda de pokemones
                        while True:
                            print("\nMenú: Introducir Pokemon a Pokedex %s" % pk.getNombre())
                            print("1- Introducir Pokemon")
                            print("2- Finalizar")
                            op = int(input("Opcion: "))
                            if op == 1:#Se añaden los objetos de pokemon en ese arbol dentro de pk
                                ip = int(input("Introduce numero del pokemon: "))
                                if arbolPokemon.find(ip) != None:
                                    fp = arbolPokemon.find(ip)
                                    print('\nSe agrego:',fp.objeto.getNombre())
                                    pk.appendPokemones(fp.dato,fp)
                                else:
                                    print("\nPokemon no existe")
                            elif op == 2:
                                break
                            else:
                                print("\nOpcion fuera de rango")
                        arbolPokedex.insert(pk.getId(),pk)#Al fin se añade todo al árbol
                    else:
                        print("\nRegion inexistente")
                else:
                    print("\nGeneracion inexistente")
            else:
                print("\nId ya utilizada")
        else:
            print("\nId no existe")
        

def baja():
    #Pokemon
    if opcion1.get()==1:
        print('Valor',opcion1.get())
        print('baja pokemon')
        #En base a la variable doy mi mensaje personalizado
        var=False
        var2=False
        n=int(caja1.get())
        lista = arbolPokedex.preorden()
        for i in range(0,len(lista),1):
            if (lista[i].objeto.getPokemones()).find(n) != None:
                var2=True

        if arbolPokemon.find(n)!=None:
            var=True

        #Mensaje que se muestra en la salida
        if var==True and var2==False:
            arbolPokemon.delete(n)
            etiqueta8.config(text='Se ha eliminado correctamente el pokemon')
            etiqueta8.place(x=300,y=290)
        elif var2==True:
            etiqueta8.config(text='No se puede eliminar pokemon en pokedex.')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe el Pokemon')
            etiqueta8.place(x=300,y=290)

    #Region
    elif opcion1.get()==2:
        print('Valor',opcion1.get())
        print('baja region')

        r=caja2.get()
        #Recorro en toda la lista
        var=False
        var2=False
        for i in range(0,region.tamaño):
            if r==region.get(i).dato.getNombre():
                var=True
                #region.remove(i)
                break
        lista = arbolPokedex.preorden()
        for j in range(0,len(lista),1):
            if r == lista[j].objeto.getRegion():
                var2=True
                var =False 
        
        #Mensaje que se muestra en la salida
        if var==True:
            region.remove(i)
            etiqueta8.config(text='Se ha eliminado correctamente la region')
            etiqueta8.place(x=300,y=290)
        elif var2==True:
            etiqueta8.config(text='No se puede eliminar region en pokedex')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la región')
            etiqueta8.place(x=300,y=290)

    #Generacion
    elif opcion1.get()==3:
        print('Valor',opcion1.get())
        print('baja generacion')
        g=caja2.get()
        #Recorro en toda la lista
        #Con esto se usa cuando no existe nada
        var=False
        var2=False
        for i in range(0,generacion.tamaño,1):
            if g==generacion.get(i).dato.getNombre():
                var=True
                break
        lista = arbolPokedex.preorden()
        for j in range(0,len(lista),1):
            if g == lista[j].objeto.getGeneracion():
                var2=True
                var =False 
        
        #Mensaje que se muestra en la salida
        if var==True:
            generacion.remove(i)
            etiqueta8.config(text='Se ha eliminado correctamente la generacion')
            etiqueta8.place(x=300,y=290)
        elif var2==True:
            etiqueta8.config(text='No se puede eliminar generacion en pokedex')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la generación')
            etiqueta8.place(x=300,y=290) 

    #Id
    elif opcion1.get()==4:
        print('Valor',opcion1.get())
        print('baja id')
        d=int(caja1.get())
        #Con la variable doy un mensaje personalizado
        var2 = False
        var=False
        if arbolId.find(d)!=None:
            if arbolPokedex.find(d) == None:
                print('Id:',arbolId.find(d).dato)
                arbolId.delete(d)
                var=True
            else:
                var2 = True

        #Mensaje que se muestra en la salida
        if var==True:
            etiqueta8.config(text='Se ha eliminado correctamente la ID')
            etiqueta8.place(x=300,y=290)
        elif var2==True:
            etiqueta8.config(text='No se puede eliminar Id en pokedex')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la id.')
            etiqueta8.place(x=300,y=290)

    #Baja pokedex
    elif opcion1.get()==5:
        os.system('cls')
        d=int(input('Dame la id a dar de baja:'))
        #Con la variable doy un mensaje personalizado
        var=False
        if arbolPokedex.find(d)!=None:
            print('\nSe ha eliminado:',arbolPokedex.delete(d))
            var=True

        #Mensaje que se muestra en la salida
        if var==True:
            pass
            #input('Se ha eliminado correctamente. Presiona Enter para continuar')
        else:
            pass
            #input('No existe la id de pokedex.Presiona Enter para continuar')

def consultar():
    #Pokemon
    if opcion1.get()==1:
        print('Valor',opcion1.get())
        print('consulta pokemon')
        
        p=int(caja1.get())
        print(p)
        var=False
        #Checo que exista en el arbol
        if arbolPokemon.find(p)!=None:
            etiqueta2.config(text='Nombre: '+str(arbolPokemon.find(p).objeto.getNombre()))
            etiqueta2.place(x=180,y=490)
            etiqueta3.config(text='Tipo 1: '+str(arbolPokemon.find(p).objeto.getTipo1()))
            etiqueta3.place(x=180,y=530)
            etiqueta4.config(text='Tipo 2: '+str(arbolPokemon.find(p).objeto.getTipo2()))
            etiqueta4.place(x=180,y=570)
            etiqueta5.config(text='Habilidad: '+str(arbolPokemon.find(p).objeto.getHabilidad()))
            etiqueta5.place(x=180,y=610)
            etiqueta6.config(text='Generacion: '+str(arbolPokemon.find(p).objeto.getGeneracion()))
            etiqueta6.place(x=180,y=650)
            etiqueta7.config(text='Region: '+str(arbolPokemon.find(p).objeto.getRegion()))
            etiqueta7.place(x=180,y=690)
            var=True

        if var==True:
            etiqueta8.config(text='Se recupero exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe el Pokemon.')
            etiqueta8.place(x=300,y=290)

    #Region
    elif opcion1.get()==2:
        print('Valor',opcion1.get())
        print('consulta region')

        r=caja2.get()
        var=False
        for i in range(0,region.tamaño,1):
            if r==region.get(i).dato.getNombre():
                etiqueta2.config(text='Año introducida:'+str(region.get(i).dato.getAño()))
                etiqueta2.place(x=180,y=490)
                var=True
                break
        if var==True:
            etiqueta8.config(text='Se recupero exitosamente')
            etiqueta8.place(x=300,y=290) 
        else:
            etiqueta8.config(text='No existe la region.')
            etiqueta8.place(x=300,y=290)

    #generacion
    elif opcion1.get()==3:
        print('Valor',opcion1.get())
        print('consulta generacion')

        g=caja2.get()
        var=False
        for i in range(0,generacion.tamaño,1):
            if g==generacion.get(i).dato.getNombre():
                etiqueta2.config(text='Consola:'+str(generacion.get(i).dato.getConsola()))
                etiqueta2.place(x=180,y=490)
                var=True
                break
        if var==True:
            etiqueta8.config(text='Se recupero exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la generacion')
            etiqueta8.place(x=300,y=290) 
 
    #Id
    elif opcion1.get()==4:
        print('Valor',opcion1.get())
        print('consulta id')

        d=int(caja1.get())
        var=False

        #Checo que exista en el arbol
        if arbolId.find(d)!=None:
            etiqueta2.config(text='Juego:'+str(arbolId.find(d).objeto.getJuego()))
            etiqueta2.place(x=180,y=490)
            var=True

        if var==True:
            etiqueta8.config(text='Se recupero exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la ID')
            etiqueta8.place(x=300,y=290)
    
    #Pokedex
    elif opcion1.get()==5:
        os.system('cls')
        d=int(input('Dame la id:'))
        var=False

        #Checo que exista en el arbol
        if arbolPokedex.find(d)!=None:
            print("\nId:",arbolPokedex.find(d).objeto.getId())
            print("Juego:",arbolPokedex.find(d).objeto.getNombre())
            print("Generacion:",arbolPokedex.find(d).objeto.getGeneracion())
            print("Region: ",arbolPokedex.find(d).objeto.getRegion())
            #input("Presione ENTER para mostrar pokemon")
            while True:
                print("\nSeleccione la manera de presentar la lista de pokemon.")
                print("1- Preorden\n2-Inorden\n3-Posorden")
                op = int(input("Opcion:"))
                subArbolPokemon = arbolPokedex.find(d).objeto.getPokemones()
                if op ==1: #Devuelve todos los pokemones dentro de del subArbol
                    for i in range(0,len(subArbolPokemon.preorden()),1):
                        print("\n#:",subArbolPokemon.preorden()[i].dato)
                        print("Nombre:",arbolPokemon.find(subArbolPokemon.preorden()[i].dato).objeto.getNombre())
                    break
                elif op ==2:
                    for i in range(0,len(subArbolPokemon.inorden()),1):
                        print("\n#:",subArbolPokemon.inorden()[i].dato)
                        print("Nombre:",arbolPokemon.find(subArbolPokemon.inorden()[i].dato).objeto.getNombre())
                    break
                elif op ==3:
                    for i in range(0,len(subArbolPokemon.posorden()),1):
                        print("\n#:",subArbolPokemon.posorden()[i].dato)
                        print("Nombre:",arbolPokemon.find(subArbolPokemon.posorden()[i].dato).objeto.getNombre())
                    break
                else:
                    print("Valor fuera de rango")

            var=True

        if var==True:
            pass
            #input('Presiona Enter para continuar')
        else:
            pass
            #input('No existe la Id. Presiona Enter para continuar')
    
def modificar():
    #Pokemon
    if opcion1.get()==1:
        print('Valor',opcion1.get())
        print('modificar pokemon')
        print('Entro a modificar')

        p=int(caja1.get())
        print('Valor de p:',p)
        nombre=caja2.get()
        tipo1=caja3.get()
        tipo2=caja4.get()
        habilidad=caja5.get()
        gen=caja6.get()
        reg=caja7.get()
        
        #print('Todo bien por aca')
        arbolPokemon.find(p).objeto.setNombre(str(nombre))
        arbolPokemon.find(p).objeto.setTipo1(str(tipo1))
        arbolPokemon.find(p).objeto.setTipo2(str(tipo2))
        arbolPokemon.find(p).objeto.setHabilidad(str(habilidad))
        arbolPokemon.find(p).objeto.setGeneracion(str(gen))
        arbolPokemon.find(p).objeto.setRegion(str(reg))

        etiqueta8.config(text='Pokemon modificado exitosamente')
        etiqueta8.place(x=300,y=290)
        
    #Region
    elif opcion1.get()==2:
        print('Valor',opcion1.get())
        print('modificar region')

        r=caja2.get()
        var=False
        for i in range(0,region.tamaño,1):
            if r==region.get(i).dato.getNombre():
                #Actualización de datos
                nuevo=Region()
                nuevo.setAño(int(caja1.get()))
                nuevo.setNombre(caja3.get())
                
                region.update(i,nuevo)
                var=True
                print('Pokedex actualzada')
                break

        if var==True:
            etiqueta8.config(text='Region modificada exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la region')
            etiqueta8.place(x=300,y=290)

    #Generacion
    elif opcion1.get()==3:
        print('Valor',opcion1.get())
        print('modificar generacion')

        g=caja2.get()
        var=False
        for i in range(0,generacion.tamaño,1):
            if g==generacion.get(i).dato.getNombre():
                #Actualización de datos
                nuevo=Generacion()
                nuevo.setConsola(caja4.get())
                nuevo.setNombre(caja3.get())
                
                generacion.update(i,nuevo)
                var=True
                print('Pokedex actualzada')
                break

        if var==True:
            etiqueta8.config(text='Generacion modificada exitosamente')
            etiqueta8.place(x=300,y=290)
        else:
            etiqueta8.config(text='No existe la generacion exitosamente')
            etiqueta8.place(x=300,y=290) 

    #ID
    elif opcion1.get()==4:
        print('Valor',opcion1.get())
        print('modificar id')

        d=int(caja1.get())
        arbolId.find(d).objeto.setJuego(caja2.get())
        print('Dato actualizado')
        print()

        etiqueta8.config(text='ID modificada exitosamente')
        etiqueta8.place(x=300,y=290) 

        #else:
        #   etiqueta8.config(text='No existe la ID')
        #   etiqueta8.place(x=400,y=400)

    #Pokedex
    elif opcion1.get()==5:
        os.system('cls')
        d = int(input("Dame el id a modificar:"))
        var = False
        if arbolPokedex.find(d)!=None:
            g = input("\nIntroduce la generacion a la que pertenece: ")
            for i in range(0,generacion.tamaño,1):
                if g==generacion.get(i).dato.getNombre():
                    var=True
                    break
            if var == True:
                var = False
                h = input("Introduce el nombre de la region: ")
                for i in range(0,region.tamaño,1):
                    if arbolPokedex.find(d).objeto.getRegion()==region.get(i).dato.getNombre():
                        var=True
                        break
                if var == True:
                    arbolPokedex.find(d).objeto.setGeneracion(g)
                    arbolPokedex.find(d).objeto.setRegion(h)
                    arbolPokedex.find(d).objeto.setPokemones(ArbolBusquedaBinaria())
                    while True:
                        print("\nMenú: Introducir Pokemon a Pokedex %s" % arbolPokedex.find(d).objeto.getNombre())
                        print("1- Introducir Pokemon")
                        print("2- Finalizar")
                        op = int(input("Opcion: "))
                        if op == 1:
                            ip = int(input("Introduce numero del pokemon: "))
                            if arbolPokemon.find(ip) != None:
                                fp = arbolPokemon.find(ip)
                                print('Se agrego:',fp.objeto.getNombre())
                                arbolPokedex.find(d).objeto.appendPokemones(fp.dato,fp)
                            else:
                                print("\nPokemon no existe")
                        elif op == 2:
                            break
                        else:
                            print("\nOpcion fuera de rango")
                else:
                    print("\nRegion inexistente")
            else:
                print("\nGeneracion inexistente")
        if var==True:
            pass
            #input('Presiona Enter para continuar')
        else:
            pass
            #input('No existe la id. Presiona Enter para continuar') 

def reporte():
    #Pokemon
    os.system('cls')
    if opcion1.get()==1:
        print("Selecciona el tipo de recorrido a usar para hacer la consulta:")
        print('1.Preorder')
        print('2.Inorden')
        print('3.Posorden')
        print("Opcion:",end='')
        recorrido=int(input())
        
        #Son listas lo que devuelve los metodos, he ahi que se use for
        #Preorden
        if recorrido==1:
            os.system('cls')
            for i in range(0,len(arbolPokemon.preorden()),1):
                print("#:",arbolPokemon.preorden()[i].objeto.getNumero())
                print("Nombre:",arbolPokemon.preorden()[i].objeto.getNombre())
                print("Tipo 1:",arbolPokemon.preorden()[i].objeto.getTipo1())
                if arbolPokemon.preorden()[i].objeto.getTipo1()!=None:
                    print("Tipo 2:",arbolPokemon.preorden()[i].objeto.getTipo2())
                print("Habilidad:",arbolPokemon.preorden()[i].objeto.getHabilidad())
                print("Generacion:",arbolPokemon.preorden()[i].objeto.getGeneracion())
                print("Region:",arbolPokemon.preorden()[i].objeto.getRegion())
                print()

        #Inorden
        elif recorrido==2:
            os.system('cls')
            for i in range(0,len(arbolPokemon.inorden()),1):
                print("#:",arbolPokemon.inorden()[i].objeto.getNumero())
                print("Nombre:",arbolPokemon.inorden()[i].objeto.getNombre())
                print("Tipo 1:",arbolPokemon.inorden()[i].objeto.getTipo1())
                if arbolPokemon.inorden()[i].objeto.getTipo1()!=None:
                    print("Tipo 2:",arbolPokemon.inorden()[i].objeto.getTipo2())
                print("Habilidad:",arbolPokemon.inorden()[i].objeto.getHabilidad())
                print("Generacion:",arbolPokemon.inorden()[i].objeto.getGeneracion())
                print("Region:",arbolPokemon.inorden()[i].objeto.getRegion())
                print()

        #Posorden
        elif recorrido==3:
            os.system('cls')
            for i in range(0,len(arbolPokemon.posorden()),1):
                print("#:",arbolPokemon.posorden()[i].objeto.getNumero())
                print("Nombre:",arbolPokemon.posorden()[i].objeto.getNombre())
                print("Tipo 1:",arbolPokemon.posorden()[i].objeto.getTipo1())
                if arbolPokemon.posorden()[i].objeto.getTipo1()!=None:
                    print("Tipo 2:",arbolPokemon.posorden()[i].objeto.getTipo2())
                print("Habilidad:",arbolPokemon.posorden()[i].objeto.getHabilidad())
                print("Generacion:",arbolPokemon.posorden()[i].objeto.getGeneracion())
                print("Region:",arbolPokemon.posorden()[i].objeto.getRegion())
                print()
        else:
            pass
            #input('Opcion fuera de rango')

        #input('Presiona Enter para continuar')
        

    #Region
    elif opcion1.get()==2:
        for i in range(0,region.tamaño,1):
            print('Año introducida:',region.get(i).dato.getAño())
            print('Nombre de la región:',region.get(i).dato.getNombre())
            print()
        #input('Presiona Enter para continuar')

    #Generación
    elif opcion1.get()==3:
        for i in range(0,generacion.tamaño,1):
            print('Consola de la región:',generacion.get(i).dato.getConsola())
            print('Nombre de la generación:',generacion.get(i).dato.getNombre())
            print()
        #input('Presiona Enter para continuar')

    #Id
    if opcion1.get()==4:
        print("Selecciona el tipo de recorrido a usar para hacer la consulta:")
        print('1.Preorder')
        print('2.Inorden')
        print('3.Posorden')
        print("Opcion:",end='')
        recorrido=int(input())
        
        #Son listas lo que devuelve los metodos, he ahi que se use for
        #Preorden
        if recorrido==1:
            os.system('cls')
            for i in range(0,len(arbolId.preorden()),1):
                print('ID:',arbolId.preorden()[i].objeto.getNumero())
                print("Juego:",arbolId.preorden()[i].objeto.getJuego())
                print()

        #Inorden
        elif recorrido==2:
            os.system('cls')
            for i in range(0,len(arbolId.inorden()),1):
                print('ID:',arbolId.inorden()[i].objeto.getNumero())
                print("Juego:",arbolId.inorden()[i].objeto.getJuego())
                print()

        #Posorden
        elif recorrido==3:
            os.system('cls')
            for i in range(0,len(arbolId.posorden()),1):
                print('ID:',arbolId.posorden()[i].objeto.getNumero())
                print("Juego:",arbolId.posorden()[i].objeto.getJuego())
                print()
        else:
            pass
            #input('Opcion fuera de rango')

        #input('Presiona Enter para continuar')     
        

    #Pokedex
    elif opcion1.get()==5:
        print("Selecciona el tipo de recorrido a usar para hacer la consulta:")
        print('1.Preorder')
        print('2.Inorden')
        print('3.Posorden')
        print("Opcion:",end='')
        recorrido=int(input())
        
        #Son listas lo que devuelve los metodos, he ahi que se use for
        #Preorden
        if recorrido==1:
            for i in range(0,len(arbolPokedex.preorden()),1):
                print("Id:",arbolPokedex.preorden()[i].objeto.getId())
                print("Juego:",arbolPokedex.preorden()[i].objeto.getNombre())
                print()

        #Inorden
        elif recorrido==2:
            for i in range(0,len(arbolPokedex.inorden()),1):
                print("Id:",arbolPokedex.inorden()[i].objeto.getId())
                print("Juego:",arbolPokedex.inorden()[i].objeto.getNombre())
                print()

        #Posorden
        elif recorrido==3:
            for i in range(0,len(arbolPokedex.posorden()),1):
                print("Id:",arbolPokedex.posorden()[i].objeto.getId())
                print("Juego:",arbolPokedex.posorden()[i].objeto.getNombre())
                print()
        else:
            pass
            #input('Opcion fuera de rango')

        #input('Presiona Enter para continuar')


######################################################################
######################################################################

ventana = Tk()
num2=DoubleVar()
res = DoubleVar()

num1=IntVar()
cadena1=StringVar()
cadena2=StringVar()
cadena3=StringVar()
cadena4=StringVar()
cadena5=StringVar()
cadena6=StringVar()

opcion1=IntVar()
opcion2=IntVar()

#*--------------------------------

ventana.geometry("678x780")
ventana.title("Pokedex")
ventana.iconbitmap('Grafico\logo.ico')
#fondo
bg = PhotoImage(file='Grafico\poked3.png')
my_label = Label(ventana, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
ventana.resizable(False, False)


#Etiquetas #listo
etiqueta1 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Numero:")  #x=400,y=80 #, bg="white"
etiqueta1.place(x=180,y=450)
etiqueta2 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Nombre:") #x=400,y=120
etiqueta2.place(x=180,y=490)
etiqueta3 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Tipo 1:")  #x400,y=160
etiqueta3.place(x=180,y=530)
etiqueta4 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Tipo 2:") #x=400,y=200
etiqueta4.place(x=180,y=570)
etiqueta5 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Habilidad:") #x=400,y=240
etiqueta5.place(x=180,y=610)
etiqueta6 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Generacion:") #x=400,y=280
etiqueta6.place(x=180,y=650)
etiqueta7 = Label(ventana,bg='white',font='Arial 10 italic bold',text="Region:") #x=400,y=320
etiqueta7.place(x=180,y=690)
etiqueta8 = Label(ventana,bg='white',font='Arial 10 italic bold',text="")
etiqueta8.place(x=180,y=730)


#Cajas #listo
caja1=Entry(ventana,textvariable=num1)    #x=480,y=80
caja1.place(x=355,y=450)
caja2=Entry(ventana,textvariable=cadena1) #x=480,y=120
caja2.place(x=355,y=490)
caja3=Entry(ventana,textvariable=cadena2) #x=480,y=160
caja3.place(x=355,y=530)
caja4=Entry(ventana,textvariable=cadena3) #x=480,y=200
caja4.place(x=355,y=570)
caja5=Entry(ventana,textvariable=cadena4) #x=345,y=610
caja5.place(x=355,y=610)
caja6=Entry(ventana,textvariable=cadena5) #x=345,y=650
caja6.place(x=355,y=650)
caja7=Entry(ventana,textvariable=cadena6) #x=345,y=690
caja7.place(x=355,y=690)

#Boton
boton1=Button(ventana,text="Seleccionar",command=seleccionar)
boton1.place(x=200,y=290)
boton2=Button(ventana,text="Agregar",command=agregar)
boton2.place(x=550,y=450)
boton3=Button(ventana,text="Dar de baja",command=baja)
boton3.place(x=550,y=450)
boton4=Button(ventana,text="Consultar",command=consultar)
boton4.place(x=550,y=450)
boton5=Button(ventana,text="Modificar",command=modificar)
boton5.place(x=550,y=450)
boton6=Button(ventana,text="Generar reporte",command=reporte)
boton6.place(x=550,y=450)

#RadioButton
#Clase #listo
radio1=Radiobutton(ventana,bg='white',font='Arial',text="Pokemon",value=1,variable=opcion1)
radio1.place(x=150,y=80)
radio2=Radiobutton(ventana,bg='white',font='Arial',text="Region",value=2,variable=opcion1)
radio2.place(x=150,y=120)
radio3=Radiobutton(ventana,bg='white',font='Arial',text="Generacion",value=3,variable=opcion1)
radio3.place(x=150,y=160)
radio4=Radiobutton(ventana,bg='white',font='Arial',text="ID",value=4,variable=opcion1)
radio4.place(x=150,y=200)
radioF=Radiobutton(ventana,bg='white',font='Arial',text="Pokedex",value=5,variable=opcion1)
radioF.place(x=150,y=240)

#Accion #texto #listo
radio5=Radiobutton(ventana,bg='white',font='Arial',text="Agregar",value=1,variable=opcion2)
radio5.place(x=350,y=80)
radio6=Radiobutton(ventana,bg='white',font='Arial',text="Dar de baja",value=2,variable=opcion2)
radio6.place(x=350,y=120)
radio7=Radiobutton(ventana,bg='white',font='Arial',text="Consultar",value=3,variable=opcion2)
radio7.place(x=350,y=160)
radio8=Radiobutton(ventana,bg='white',font='Arial',text="Modificar",value=4,variable=opcion2)
radio8.place(x=350,y=200)
radio8=Radiobutton(ventana,bg='white',font='Arial',text="Generar reporte",value=5,variable=opcion2)
radio8.place(x=350,y=240)


ventana.mainloop()