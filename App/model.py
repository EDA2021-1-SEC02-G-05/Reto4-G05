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


from DISClib.DataStructures.chaininghashtable import newMap
from os import name
import config as cf
import re
from DISClib.ADT import list as lt
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Graphs import scc as kosa
from DISClib.Algorithms.Graphs import bfs as bfs
from DISClib.DataStructures import listiterator as it
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
    dicci["grafico2"]=gr.newGraph(datastructure='ADJ_LIST',directed= False,size=14000,comparefunction=None)
    dicci["lista"]=lt.newList()
    dicci["tabla"]=mp.newMap()
    dicci["paises"]=lt.newList()
    dicci["pp"]=mp.newMap()

    dicci["mayores"]=mp.newMap()
    return dicci

def agregarvertices(dicci,ver):
        
    lis=[]
    lola=[]
    lis.append(lola)
    lis[0].append(ver)
    mp.put(dicci["tabla"],ver["landing_point_id"],lis)
    carlos=""
    for i in ver["name"]:
        carlos+=i
        if i==",":
            carlos= ""
    carlos=carlos.replace(" ","")

    if mp.contains(dicci["pp"],carlos):

        jef=mp.get(dicci["pp"],carlos)
        lis = me.getValue(jef)
        lt.addLast(lis,ver["landing_point_id"])

    else:

        lis=lt.newList()
        mp.put(dicci["pp"],carlos,lis)
        lt.addLast(lis,ver["landing_point_id"])

            
    return dicci


def union(dicci,verti):

    elbicho = verti["cable_name"]
    
   

    vela = str(verti["origin"])+"-"+str(elbicho)

    jef= mp.get(dicci["tabla"],verti["origin"])
    lis = me.getValue(jef)
    lis.append(vela) 

    vela2 = str(verti["destination"])+"-"+str(elbicho)
    jef2= mp.get(dicci["tabla"],verti["destination"])
    lis2 = me.getValue(jef2)
    lis2.append(vela2) 




    return dicci
   









def completo(dicci, verti):

    kun= verti["cable_name"]
    
    
    vela = str(verti["origin"])+"-"+str(kun)
    riquelme=str(verti["destination"])+"-"+str(kun)

    gr.insertVertex(dicci["grafico"],vela)
    gr.insertVertex(dicci["grafico"],riquelme)


    return dicci



def completo1(dicci, verti):

    elbicho = verti["cable_length"]
    kun= verti["cable_name"]

    
    if elbicho == "n.a.":

        elbicho = 0
        vela = str(verti["origin"])+"-"+str(kun)
        riquelme=str(verti["destination"])+"-"+str(kun)

        gr.addEdge(dicci['grafico'],vela,riquelme,float(elbicho))

        


    else:

        elbicho1 = elbicho[:-3]

        elbicho1 = elbicho1.replace(",","")

        vela1 = str(verti["origin"])+"-"+str(kun)
        riquelme1=str(verti["destination"])+"-"+str(kun)

        gr.addEdge(dicci['grafico'],vela1,riquelme1,float(elbicho1))


    return dicci





def agregarpaises(dicci,pp):


    lt.addLast(dicci["paises"],pp)

    return dicci



def mapa(dicci):
    


    chabal= mp.valueSet(dicci["tabla"])

    iterador1 = it.newIterator(chabal)

    while it.hasNext(iterador1):

        actual1 = it.next(iterador1)

        ronney=None

        for i in actual1[1:]:

            if ronney == None:

                ronney=i

            else:
                gr.addEdge(dicci['grafico'],ronney,i,0.1)
                ronney= i

    return dicci
       
 

def requerimiento1(dicci,lad1,lad2):

    k = kosa.KosarajuSCC(dicci["grafico"])

    numclusteres = kosa.connectedComponents(k)

    mismocluster = kosa.stronglyConnected(k,lad1,lad2)

    return numclusteres,mismocluster


def requerimiento2(dicci):
    lista = []

    chabal= mp.keySet(dicci["tabla"])

    iterador1 = it.newIterator(chabal)

    while it.hasNext(iterador1):

        actual1 = it.next(iterador1)

        jef2= mp.get(dicci["tabla"],actual1)
        lis2 = me.getValue(jef2)

        numero= gr.degree(dicci["grafico"],lis2[1])


        lista.append(("Nombre del pais: "+str(lis2[0][0]["name"])+" con el identificador: "+str(lis2[1])+", con su numero total de conexiones es: "+str(numero)))





        
 

    return lista


def requerimiento3(dicci,paisA,paisB):
    lili=[]
    jef1=mp.get(dicci["pp"],paisA)
    lis1 = me.getValue(jef1)
    tulio=lt.getElement(lis1,1)

    jef11=mp.get(dicci["tabla"],tulio)
    lis11 = me.getValue(jef11)
    lis11=lis11[1]




    jef=mp.get(dicci["pp"],paisB)
    lis = me.getValue(jef)
    julio=lt.getElement(lis,1)


    gordo=mp.get(dicci["tabla"],julio)
    lisa = me.getValue(gordo)
    lisa=lisa[1]
    
    lili.append(lisa)
    lili.append(lis11)


    Rutas=djk.Dijkstra(dicci["grafico"],lis11)

    Minima = djk.distTo(Rutas,lisa)

    camino = djk.pathTo(Rutas,lisa)

   


    return Minima








def requerimiento5(dicci):
    lili=[]
    mache="4181-2Africa"
    parce=(mache.split("-"))[0]
    jeff= mp.get(dicci["tabla"],parce)
    lis = me.getValue(jeff)
    vela=lis[0][0]["name"]
    lili.append(vela)

    pepe=gr.adjacentEdges(dicci["grafico"],mache)

    iterador1 = it.newIterator(pepe)

    while it.hasNext(iterador1):

        actual1 = it.next(iterador1)

        


        carlos= actual1["vertexA"]
        carlos=(carlos.split("-"))[0]
    

        jef2= mp.get(dicci["tabla"],carlos)
        lis2 = me.getValue(jef2)
        quique=lis2[0][0]["name"]
        carlo=""

        for i in quique:

            carlos+=i

            if i==",":

                carlos= ""


        carlos=carlos.replace(" ","")

        if carlos not in lili:


            lili.append(carlos)
            


    return lili



    






        


    










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
