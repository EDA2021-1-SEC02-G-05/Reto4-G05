"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT.graph import gr, vertices
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información del grafo")
    print("2- ")

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
        verti=gr.numVertices(dicci["grafico"])#numero de vertices
        arc= gr.numEdges(dicci["grafico"])#numero de arcos
        pais= lt.size(dicci["paises"])#tamaño lista (numero de paises)
        infoultimo=lt.getElement(dicci["paises"],pais)#saca la información del ultimo pais del archivo
        infoultimo= "La poblacion del ultimo pais es",infoultimo["Population"]," y el numero de usuarios de internet son: ",infoultimo["Internet users"]
    
        
        ultimo=lt.getElement(dicci["lista"],verti)
        ultimo=("Ultimo landing point cargado : "+str(ultimo["landing_point_id"])+", Nombre del landing point: "+str(ultimo["name"])+", Latitud :"+str(ultimo["latitude"])+", Longitud: "+str(ultimo["longitude"]))
        print("Cargando información de los archivos ....")
        print("El numero total de landing points: "+str(verti))
        print("El numero total de conexiones son : "+str(arc))
        print("El numero total de paises es: ",pais)
        print(ultimo)
        print(infoultimo)

    elif int(inputs[0]) == 2:
        pass
    else:
        sys.exit(0)
sys.exit(0)
