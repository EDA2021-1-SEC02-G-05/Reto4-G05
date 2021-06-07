import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
from DISClib.ADT.graph import gr
assert cf

default_limit = 1000 
sys.setrecursionlimit(default_limit*10) 

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información del grafo")
    print("2- Cargar requerimiento 1")
    print("3- Cargar requerimiento 2")
    print("4- Cargar requerimiento 3")
    print("5- Cargar requerimiento 4")
    print("6- Cargar requerimiento 5")
    print("7- Cargar requerimiento 6")

dicci = None
files="landing_points.csv"
files2='connections.csv'
files3="countries.csv"
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        dicci=controller.init()
        dicci=controller.loadvertices(dicci,files)
        dicci=controller.loadarcos(dicci,files2)
        dicci=controller.loadpais(dicci,files3)
        dicci=controller.loadarcos1(dicci,files2)
        dicci=controller.loadmapa(dicci)
        





        verti=gr.numVertices(dicci["grafico"])#numero de vertices
        arc= gr.numEdges(dicci["grafico"])#numero de arcos
        pais= lt.size(dicci["paises"])#tamaño lista (numero de paises)
        infoultimo=lt.getElement(dicci["paises"],pais)#saca la información del ultimo pais del archivo
        infoultimo= ("La poblacion del ultimo pais es: "+str(infoultimo["Population"])+(" y el numero de usuarios de internet son: "+str(infoultimo["Internet users"])))
        pp=mp.keySet(dicci["pp"])
        



        print("Cargando información de los archivos ....")
        print("El numero total de landing points: "+str(verti))
        print("El numero total de conexiones son : "+str(arc))
        print("El numero total de paises es: ",pais)
        print(infoultimo)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")


    elif int(inputs[0]) == 2:

        lad1 = input("Ingrese el primer landinf point: ")
        lad2 = input ("Ingrese el segundo landing point: ")
        
        g = controller.loadrequerimiento1(dicci,lad1,lad2)

        print("El numero total de clusteres es: "+str(g[0]))
        print("Los clusteres "+str(lad1)+str(" y ")+str(lad2)+str(" son ")+str(g[1]))
    
    elif int(inputs[0]) == 3:

        f = controller.loadrequerimiento2(dicci)
        
        
        print(f)

    elif int(inputs[0]) == 4:

        paisA=input(" Ingrese el nombre del pais de su interes: ")
        paisB=input(" Ingrese el nombre del pais de su interes: ")

        h = controller.loadrequerimiento3(dicci,paisA,paisB)
        
        print("La distancia de conexion entre cada par de vertices consecutivos es: ",h)

    elif int(inputs[0]) == 5:

        c = controller.loadrequerimiento4(dicci)

        print("El numero de nodos conectados a la red de expansión minima es: "+str(c[0]))
        print("El costo total de la red de expasión minima es :"+str(c[1]))
        print(c[2])


    elif int(inputs[0]) == 6:

        mache=input("  Ingrese el nombre del vertice de su interes: ")

        c = controller.loadrequerimiento5(dicci,mache)
        longi=len(c)

        print(" La cantidad de paises afectado es "+str(longi))

        print(c)

    elif int(inputs[0]) == 7:

        pais=input(" Ingrese el nombre del pais de su interes: ")
        cable=input(" Ingrese el nombre del cable de su interes: ")

        r = controller.loadrequerimiento6(dicci,pais,cable)

        print(r)
    else:
        sys.exit(0)
