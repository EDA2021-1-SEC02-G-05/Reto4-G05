﻿"""
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


    return dicci

def agregarvertices(dicci,ver):

    gr.insertVertex(dicci["grafico"],ver["landing_point_id"])
    lt.addLast(dicci["lista"],ver)
    

    return dicci

def agregararcos(dicci,verti):

    gr.addEdge(dicci['grafico'],verti["destination"],verti["origin"],verti["cable_length"])


    return dicci

def agregarpaises(dicci,pp):

    lt.addLast(dicci["paises"],pp)
    


    return dicci






        




    










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
