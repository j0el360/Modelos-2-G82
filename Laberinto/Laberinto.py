"""Se crea el laberinto (en este caso es de 8x6)
    si se desea agregar otra fila o columna se debe hacer desde este punto
"""
laberinto=[["y", 1, 1, 1, 0, 0, 0, 0],
          [ 0, 1, 0, 0, 1, 0, 0, 0 ],
          [ 1, 0, 1, 0, 0, 0, 0, 0 ],
          [ 1, 1, 0, 0, 0, 1, 0, 0 ],
          [ 0, 0, 0, 1, 0, 0, 0, 0 ],
          [ 0, 0, 0, 1, 0, 0, 0, 0 ],
          [ 0, 1, 0, 0, 0, 0,"x", 0]
          ];

"""Creamos una clase nodo para el manejo de arboles"""
class Nodo():
    def __init__(self,valor,posicion,hijos=[]):
        self.valor=valor
        self.posicion = posicion
        self.hijos=hijos

    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        
    def setPosicion(self,posicion):
        self.posicion=posicion

    def setHijos(self,hijos):
        self.hijos=hijos


def buscar(arbol,posicion):
    if arbol==None:
        return False
    if arbol.posicion==posicion:
        return True
    return buscarhijos(arbol.hijos,posicion) 



def buscarhijos(hijos,posicion):
    if hijos==[]:
        return False
    return buscar(hijos[0],posicion) or buscarhijos(hijos[1:],posicion)



def buscarValor(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscarhijosValor(arbol.hijos,valor) 


def buscarhijosValor(hijos,valor):
    if hijos==[]:
        return False
    return buscarValor(hijos[0],valor) or buscarhijosValor(hijos[1:],valor)


def imprimir(arbol):
    if(arbol==None):
        print("None")
    else:
        print(arbol.posicion)
        if(len(arbol.hijos)>0):
            for i in arbol.hijos:
                imprimir(i)     

"""Buscamos la posicion x,y en la que se encuentra la 'x'"""
def buscarX(lista):
   for x in lista:
       for y in range(len(x)):
           if x[y] == "x":
               colocarArbol(lista.index(x),y) 

raiz=Nodo(0,0,[])
arbol=Nodo(0,0,[])
def colocarArbol(x,y):
        raiz.setPosicion((x,y))
        arbol.setPosicion((x,y))
        raiz.setHijos([verIzquierda(x,y,arbol),verAbajo(x,y,arbol),verArriba(x,y,arbol),verDerecha(x,y,arbol)])

   
"""Se evaluan los movimentos hacia la derecha, izquierda, abajo y arriba mediante el uso de arboles"""
def verDerecha(x,y,nodo):
    print((x,y),"der:")
    if(y+1<=len(laberinto[x])-1 and laberinto[x][y+1]!=1):
        if(buscar(nodo,(x,y+1))!=True):
            nodo.agregarHijo(Nodo(laberinto[x][y+1],(x,y+1),[]))
            return Nodo(laberinto[x][y+1],(x,y+1),[verAbajo(x,y+1,nodo),verArriba(x,y+1,nodo),verIzquierda(x,y+1,nodo),verDerecha(x,y+1,nodo)])
        else:
            return None
    else:
        return None
 
def verIzquierda(x,y,nodo):
    print((x,y),"izq:")
    if(y-1>=0 and laberinto[x][y-1]!=1):
        if(buscar(nodo,(x,y-1))!=True):
            nodo.agregarHijo(Nodo(laberinto[x][y-1],(x,y-1),[]))
            return Nodo(laberinto[x][y-1],(x,y-1),[verAbajo(x,y-1,nodo),verArriba(x,y-1,nodo),verIzquierda(x,y-1,nodo),verDerecha(x,y-1,nodo)])
        else:
            return None
    else:
        return None
 
def verAbajo(x,y,nodo):
    print((x,y),"abj:")
    if(x+1<=len(laberinto)-1 and laberinto[x+1][y]!=1):
        if(buscar(nodo,(x+1,y))!=True):
            nodo.agregarHijo(Nodo(laberinto[x+1][y],(x+1,y),[]))
            return Nodo(laberinto[x+1][y],(x+1,y),[verAbajo(x+1,y,nodo),verArriba(x+1,y,nodo),verIzquierda(x+1,y,nodo),verDerecha(x+1,y,nodo)])
        else:
            return None
    else:
        return None
 
def verArriba(x,y,nodo):
    print((x,y),"arr:")
    if(x-1>=0 and laberinto[x-1][y]!=1):
        if(buscar(nodo,(x-1,y))!=True):
            nodo.agregarHijo(Nodo(laberinto[x-1][y],(x-1,y),[]))
            return Nodo(laberinto[x-1][y],(x-1,y),[verAbajo(x-1,y,nodo),verArriba(x-1,y,nodo),verAbajo(x-1,y,nodo),verDerecha(x-1,y,nodo)])
        else:
            return None
    else:
        return None

    """Se imprime el laberinto"""
for i in range(len(laberinto)):
    print(laberinto[i])
    

buscarX(laberinto)

if(buscarValor(raiz,"y")==True):
    print("Si tiene solución")
else:
    print("No tiene solución")





