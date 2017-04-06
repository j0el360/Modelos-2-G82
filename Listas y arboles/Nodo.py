
class Nodo:
    nodoIzq=None;
    nodoDer=None;
    dato=0;
    def __init__(self,valor):
        self.dato=valor;
        self.nodoIzq=None;
        self.nodoDer=None;
        self.raz=None;


raiz=None;
def inorden(actual):
    if(actual!=None):
        inorden(actual.nodoIzq);
        print(actual.dato);
        inorden(actual.nodoDer);

def posorden(actual):
    if(actual!=None):
        inorden(actual.nodoIzq);        
        inorden(actual.nodoDer);
        print("in"+actual.dato);

def preorden(actual):
    if(actual!=None):
        print("in"+actual.dato);
        inorden(actual.nodoIzq);        
        inorden(actual.nodoDer);



def insertar(actual,dato):
    global raiz;
    if(raiz==None):
        raiz=Nodo(dato);
        actaul=raiz;
    elif(actual.dato<dato):
        if(actual.nodoDer==None):
            print(dato);
            actual.Nododer=Nodo(dato);
        else:
            insertar(actual.nodoDer,dato)
    elif(actual.dato>dato):
        if(actual.nodoIzq==None):
            actual.nodoIzq=Nodo(dato);
        else:
            insertar(actual.nodoIzq,dato);
    else:
        print("El nodo ya existe")

def buscar(raiz,valor):
    if(raiz==None):
        return False;
    elif (raiz.dato==valor):
        print("si")
        return True;
    else:
        return buscar(raiz.nodoDer,valor) or buscar(raiz.nodoIzq,valor);




insertar(raiz,10);
insertar(raiz,5);
insertar(raiz,3);
insertar(raiz,7);
insertar(raiz,20);
insertar(raiz,15);
insertar(raiz,25);
insertar(raiz,17);


buscar(raiz,7);

