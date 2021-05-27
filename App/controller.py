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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    dicci = model.newgraph()
    return dicci




def loadvertices(dicci,filess):

    mapfile1 = cf.data_dir + "landing_points.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8"),
                                delimiter=",")
    
    for ver in input_file:

        model.agregarvertices(dicci,ver)

  
    return dicci

def loadarcos(dicci,filess2):

    mapfile1 = cf.data_dir + "connections.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8-sig"),
                                delimiter=",")
    
    for verti in input_file:

        model.agregararcos(dicci,verti)

    return dicci






# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
