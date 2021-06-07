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
from DISClib.Algorithms.Graphs import prim as mst
from DISClib.ADT import queue as col
assert cf


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
    jef1=mp.get(dicci["pp"],paisA)
    lis1 = me.getValue(jef1)
    tulio=lt.getElement(lis1,1)

    jef11=mp.get(dicci["tabla"],tulio)
    lis11 = me.getValue(jef11)

    log=float(lis11[0][0]["longitude"])
    lat=float(lis11[0][0]["latitude"])



    pp1=(log,lat)


    jef=mp.get(dicci["pp"],paisB)
    lis = me.getValue(jef)
    julio=lt.getElement(lis,1)


    gordo=mp.get(dicci["tabla"],julio)
    lisa = me.getValue(gordo)
    log1=float(lisa[0][0]["longitude"])
    lat1=float(lisa[0][0]["latitude"])



 

    pp2=(log1,lat1)



    
    

    dm=hs.haversine(pp1,pp2)

    jack= (" La distancia total entre  "+str(paisA)+"  y "+str(paisB)+" es: "+ str(dm))



    return jack



def requerimiento4(dicci):

    prim = mst.PrimMST(dicci["grafico"]) # devuelve el search

    camino = mst.edgesMST(dicci["grafico"],prim)# camino minimo

    #rta

    tamano = col.size(camino["mst"])

    peso = mst.weightMST(dicci["grafico"],prim) # peso del camino minimo

    valores = mp.valueSet(prim["distTo"])

    iterador = it.newIterator(valores)

    lista = []
    while it.hasNext(iterador):

        actu = it.next(iterador)

        lista.append(actu)

        x = 0
        c = []
        while x <len(lista):

            c.append(lista[x])

            x+=3

    return tamano,peso,max(c)

def requerimiento5(dicci,mache):
    lili=[]
    lulu=[]
    coco=[]
   
    pepe=gr.adjacentEdges(dicci["grafico"],mache)

    iterador1 = it.newIterator(pepe)

    while it.hasNext(iterador1):

        actual1 = it.next(iterador1)


        juancho= actual1["vertexA"]


        carlos= actual1["vertexA"]
        carlos=(carlos.split("-"))[0]

        

        jef2= mp.get(dicci["tabla"],carlos)
        lis2 = me.getValue(jef2)
        quique=lis2[0][0]["name"]
        carlos=""

        for i in quique:

            carlos+=i

            if i==",":

                carlos= ""


        carlos=carlos.replace(" ","")

        jarras=(juancho, carlos)

        if jarras not in lulu:

            lulu.append(jarras)


    origen=lulu[0][0]
    origen=(origen.split("-"))[0]
    
    orr= mp.get(dicci["tabla"],origen)
    lla = me.getValue(orr)
    la1=lla[0][0]["latitude"]
    log1=lla[0][0]["longitude"]

    lola1=(float(la1),float(log1))


    lulu=lulu[1:]

    for i in lulu:

        orgg=(i[0].split("-"))[0]


        orr= mp.get(dicci["tabla"],orgg)
        lal = me.getValue(orr)
        la2=lal[0][0]["latitude"]
        log2=lal[0][0]["latitude"]

        lola2=(float(la2),float(log2))

        dm=hs.haversine(lola1,lola2)

        coco.append((" el pais "+str(i[1])+ " estara afectado, y cuenta con una distancia " +str(dm)+" km"))


    return coco


def nuevo(dicci,verti):

    if mp.contains(dicci["nuevo"],verti["cable_name"]):

        jef=mp.get(dicci["nuevo"],verti["cable_name"])
        lis = me.getValue(jef)
        lt.addLast(lis,verti)

    else:

        lisa=lt.newList()
        lt.addLast(lisa,verti)
        mp.put(dicci["nuevo"],verti["cable_name"],lisa)

    return dicci

def tablapais(dicci,pp):

    if mp.contains(dicci["tablita"],pp["CountryName"]):

        jef=mp.get(dicci["tablita"],pp["CountryName"])
        lis = me.getValue(jef)
        lt.addLast(lis,pp)

    else:

        lisa=lt.newList()
        lt.addLast(lisa,pp)
        mp.put(dicci["tablita"],pp["CountryName"],lisa)

    return dicci

    

def requerimiento6(dicci,pais,cable):

    lista = []
    lista2 = []

    breve = dicci["tablita"]
    llavesita = mp.get(breve,pais)
    valores = me.getValue(llavesita)

    valido = dicci["nuevo"]
    llave = mp.get(valido,cable)
    valor = me.getValue(llave)

    iterador1 = it.newIterator(valor)

    while it.hasNext(iterador1):

        actual = it.next(iterador1)

        iterador2 = it.newIterator(valores)

        while it.hasNext(iterador2):

            actual2 = it.next(iterador2)

            lista.append(actual)
            lista2.append(actual2)

    o=[]
    for i in lista:
        for x in lista2:

            cap= i["capacityTBPS"].replace(".","")
            inte = x["Internet users"].replace(".","")

            rta= float(cap)/float(inte)

    return rta

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
