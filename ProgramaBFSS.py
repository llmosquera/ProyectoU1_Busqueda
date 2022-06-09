from doctest import master
import collections

#Se establecerá una clase que se encontrará el grafo y su logica
class Grafo:
    def __init__(self, innumeroNodos, inPosicionInicial):
        #Guarda el numero nodos del grafo (tamaño)
        self.numeroNodos=innumeroNodos
        #Guarda los diferentes nombres de los nodos del grafo
        self.nombreNodos=[]
        #Establece la posición actual del grafo
        self.raiz=inPosicionInicial
    
   