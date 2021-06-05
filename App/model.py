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
import re
import haversine as hs
from DISClib.ADT import list as lt
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
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

    dicci["mayores"]=mp.newMap()
    return dicci

def agregarvertices(dicci,ver):
        
    lis=[]
    lola=[]
    lis.append(lola)
    lis[0].append(ver)
    mp.put(dicci["tabla"],ver["landing_point_id"],lis)
    
    
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
    lola=[]

    Rutas=djk.Dijkstra(dicci["grafico"],paisA)


    camino = djk.pathTo(Rutas,paisB)

    iterador1 = it.newIterator(camino)

    while it.hasNext(iterador1):

        actual1 = it.next(iterador1)


        coco=actual1["vertexA"]
        coco = (coco.split("-"))[0] 
        lili.append(coco)

    jef2= mp.get(dicci["tabla"],lili[0])
    lis2 = me.getValue(jef2)

    lat=float(lis2[0][0]["latitude"])
    log=float(lis2[0][0]["longitude"])


    jef= mp.get(dicci["tabla"],lili[1])
    lis = me.getValue(jef)

    lat1=float(lis[0][0]["latitude"])
    log1=float(lis[0][0]["longitude"])




    lol= (lat,log)
    lol2=(lat1,log1)
    dm=hs.haversine(lol,lol2)




    


    return lili








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
