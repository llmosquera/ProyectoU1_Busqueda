from doctest import master
import collections

#Se establecerá una clase que se encontrará el grafo y su logica
class Grafo:
    """
    Una clase que representa un grafo bfs.

    ...

    Attributes
    ----------
    innumeroNodos : int
        Establece el numero de nodos.
        
    inPosicionInicial : int
        La posicion inicial del grafo.
        
    nombreNodos : dictionary
        Establece los nombres de los diferentes nodos del grafo.
        
    raiz : str
        La posición inicial del grafo.
    
    Methods
    -------
    registrarZonas(): 
        Permite registrar los nombres de los nodos.
        
    mostrarZonas():
        Muestra el grafo completo.
        
    agregarAristas(nodo1, nodo2):
        Crea una arista entre nodos.
        
    estructurarNodos():
        Establece el formato para guardar el grafo.
        
    bfs(objetivo):
        Redirige la posicion a un nuevo elemento del grafo
    """
    def __init__(self, innumeroNodos, inPosicionInicial):
        """
        Establece la estructura del grafo.

        Parameters
        ----------
        innumeroNodos : int
            Numero de nodos 
            
        inPosicionInicial: str
            Posicion inicial del grafo

        """
        #Guarda el numero nodos del grafo (tamaño)
        self.numeroNodos=innumeroNodos
        #Guarda los diferentes nombres de los nodos del grafo
        self.nombreNodos=[]
        #Establece la posición actual del grafo
        self.raiz=inPosicionInicial
    
    #Se va a registrar el nomrbe de los diferentes nodos
    def registrarZonas(self):
        """
        Permite registrar nodos.

        Parameters
        ----------
        No se requiere parametros
            (Pide por consola el nombre de los nodos)

        Returns
        -------
        None
        """    
        #recorremos para agregar nombres al array de nombre nodos
        for nodo in range(0,self.numeroNodos,+1):
            nombre= input('Ingrese el nombre del nodo: '+str(nodo)+': ')
            self.nombreNodos.append(nombre)
        self.estructurarNodos()
        
    #Muestra el grafo completo            
    def mostrarZonas(self):
        """
        Muestra el grafo completo.

        Parameters
        ----------
        No se requiere parametros

        Returns
        -------
        Imprime el grafo completo
        """      
        print(self.dict_list)
    #Agrega aristas para unir dos nodos
    def agregarAristas(self, nodo1, nodo2):
        """
        Conecta a dos nodos mediante aristas.

        Parameters
        ----------
        nodo : str
            Nombre del nodo 
        """      
        
        self.dict_list[nodo1].add((nodo2))
        self.dict_list[nodo2].add((nodo1))
        
    #Establece un dicccionario que usa los nombres establecidos
    def estructurarNodos(self):
        """
        Estructura la estructura del grafo.

        Parameters
        ----------
        No se requiere parametros

        Returns
        -------
        La estructura del grafo a partir de nombres
        """      
        self.dict_list = {nodo: set() for nodo in self.nombreNodos}
    
    #Logica del algoritmo bfs
    def bfs(self,objetivo):
        """
        Redirige de un sitio a otro en el grafo.

        Parameters
        ----------
        objetivo: str
            Establece el nodo al que el usuario quiere dirigirse

        """    
        #establece en una variable el diccionario
        g=self.dict_list
        #agregar en forma de estructura de datos
        cola= collections.deque([self.raiz])
        #Establecer una lista de areas visitadas
        visitado=[]
        #mientras haya elementos en la cola
        while cola:
            #saca el elemento de la izquierda
            nodo = cola.popleft()
            #si el nodo no ha sido visitado
            if nodo not in visitado:
                #agregara el nodo a visitados
                visitado.append(nodo)
                #si llegamos a la respuesta nos devolverá la posicion actual
                if nodo == objetivo:
                    self.raiz=nodo
                    print(f' {visitado} ')
                    return
            #Si ha sido visitado recorrerá los elementos que se encuentran asociados al nodo
            for registro in g[nodo]:
                #si encuentra alguno que no es visitado
                if registro not in visitado:
                    #agregara a la derecha de la cola
                    cola.append(registro)
                    
        
if __name__ == "__main__":
    numeroNodos= input('Digite porfavor el numero de nodos: ')
    posicionInicial= input('Digite la posicion inicial del grafo : ')
    grafo= Grafo(int(numeroNodos),posicionInicial)
    grafo.registrarZonas()
    print('A continuación tiene que agregar las aristas al grafo')
    while True:
        nodo1=input('Digite el nodo 1 : ')
        nodo2=input('Digite el nodo 2 : ')
        grafo.agregarAristas(nodo1,nodo2)
        print('Conectando nodo '+nodo1+' con nodo '+nodo2)
        opcion= input('Digite s para ya no ingresar mas aristas: ')
        if(opcion.strip().lower()=='s'):
            break
    print('A continuacion se muestra el grafo: ')
    grafo.mostrarZonas()
    
    while True:
        print('El nodo inicial del grafo es: '+grafo.raiz)
        objetivo= input('Digite el nombre del grafo objetivo: ')
        print('El camino es : ')
        grafo.bfs(objetivo)
        opcion= input('Si desea ir a otro lado del grafo, digite s: ')
        if opcion!='s':
            break