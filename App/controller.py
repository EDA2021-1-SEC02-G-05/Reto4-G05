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

        model.union(dicci,verti)
        model.completo(dicci,verti)

    return dicci

def loadarcos1(dicci,filess2):

    mapfile1 = cf.data_dir + "connections.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8-sig"),
                                delimiter=",")
    
    for verti in input_file:

        model.completo1(dicci,verti)

        

    return dicci


def loadmapa(dicci):

    ramon= model.mapa(dicci)

    return ramon







def loadpais(dicci,pp):

    mapfile1 = cf.data_dir + "countries.csv"
    input_file = csv.DictReader(open(mapfile1, encoding="utf-8-sig"),
                                delimiter=",")
    
    for pp in input_file:

        model.agregarpaises(dicci,pp)

    return dicci





def loadrequerimiento1(dicci,lad1,lad2):

    req1 = model.requerimiento1(dicci,lad1,lad2)

    return req1[0],req1[1]

def loadrequerimiento2(dicci):

    req2 = model.requerimiento2(dicci)

    return req2

def loadrequerimiento3(dicci,paisA,paisB):

    req3 = model.requerimiento3(dicci,paisA,paisB)

    return req3


def loadrequerimiento4(dicci):

    req3 = model.requerimiento4(dicci)

    return req3[0],req3[1],req3[2]


def loadrequerimiento5(dicci,mache):

    return model.requerimiento5(dicci,mache)


def loadrequerimiento6(dicci,pais,cable):

    return model.requerimiento6(dicci,pais,cable)
