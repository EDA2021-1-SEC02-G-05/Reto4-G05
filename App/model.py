"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from os import name
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import scc as kosa
from DISClib.Algorithms.Graphs import prim as mst
from DISClib.Algorithms.Graphs import bfs as bfs
from DISClib.Utils import error as error
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newgraph():

    dicci={}

    dicci["grafico"]=gr.newGraph(datastructure='ADJ_LIST',directed= False,size=14000,comparefunction=None)
    dicci["lista"]=lt.newList()
    dicci["paises"]=lt.newList()

    dicci["mayores"]=mp.newMap()
    return dicci

def agregarvertices(dicci,ver):


    gr.insertVertex(dicci["grafico"],ver["landing_point_id"])
    lt.addLast(dicci["lista"],ver)
    

    return dicci

def agregararcos(dicci,verti):

    elbicho = verti["cable_length"]
    
    if elbicho == "n.a.":

        elbicho = 0

        gr.addEdge(dicci['grafico'],verti["destination"],verti["origin"],elbicho)

    else:

        elbicho = elbicho[:-3]

        elbicho = elbicho.replace(",","")

        elbicho = float(elbicho)

        gr.addEdge(dicci['grafico'],verti["destination"],verti["origin"],elbicho)

    return dicci

def agregarpaises(dicci,pp):

    lt.addLast(dicci["paises"],pp)

    return dicci

def requerimiento1(dicci,lad1,lad2):

    k = kosa.KosarajuSCC(dicci["grafico"])

    numclusteres = kosa.connectedComponents(k)

    mismocluster = kosa.stronglyConnected(k,lad1,lad2)

    return numclusteres,mismocluster


def requerimiento2(dicci):

    for i in range(0,lt.size(dicci["lista"])):

        rta=lt.getElement(dicci["lista"],i)

        numero = gr.degree(dicci["grafico"],rta["landing_point_id"])

        lista = []

        lista.append(("Nombre del pais: "+str(rta["name"])+" con el identificador: "+str(rta["id"])+" con su numero total de conexiones es: "+str(numero)))

        mp.put(dicci["mayores"],rta["name"],lista)

    valoresHash=mp.valueSet(dicci["mayores"])

    top1 = lt.getElement(valoresHash,1)
    top2 = lt.getElement(valoresHash,2)
    top3 = lt.getElement(valoresHash,3)
    top4 = lt.getElement(valoresHash,4)
    top5 = lt.getElement(valoresHash,5)

    return top1,top2,top3,top4,top5


def requerimiento3(dicci,paisA,paisB):

    Rutas=djk.Dijkstra(dicci["grafico"],paisA)

    Minima = djk.distTo(Rutas,paisB)

    camino = djk.pathTo(Rutas,paisB)

  
    return Minima,camino


def requerimiento4(dicci):

    prim = mst.PrimMST(dicci["grafico"])
    



    return prim








        
 








        




    










# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareStopIds(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1
