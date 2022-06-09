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
         #Se va a registrar el nomrbe de los diferentes nodos
    def registrarZonas(self):
        #recorremos para agregar nombres al array de nombre nodos
        for nodo in range(0,self.numeroNodos,+1):
            nombre= input('Ingrese el nombre del nodo: '+str(nodo)+': ')
            self.nombreNodos.append(nombre)
        self.estructurarNodos()
        
    #Muestra el grafo completo            
    def mostrarZonas(self):
    
   