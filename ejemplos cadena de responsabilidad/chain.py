class Manejador(object):
    def __init__(self,x):
        self._sucesor = x
    def setSucesor(self,sucesor):
        self._sucesor=sucesor;
        
    def getSucesor(self):        
        return self._sucesor;
    def request(self,opt):
        print ("");
        
class Manejadorbasico(Manejador):
    def request(self,opt):
        if(opt==1):
            print("Liquidacion basica");
        else:
           self.getSucesor().request(opt)

class ManejadorCatedra(Manejador):
    def request(self,opt):
        if(opt==2):
            print("Liquidacion catedra");
        else:
           self.getSucesor().request(opt)


class Manejadorhc(Manejador):
    def request(self,opt):
        if(opt==3):
            print("Liquidacion hc");
        else:
           self.getSucesor().request(opt)



class Manejadormto(Manejador):
    def request(self,opt):
        if(opt==4):
            print("Liquidacion mto");
        else:
           self.getSucesor().request(opt)    

class Manejadortco(Manejador):
    def request(self,opt):
        if(opt==5):
            print("Liquidacion tco");
        else:
           self.getSucesor().request(opt)    

class ManejadorHonorarios(Manejador):
    def request(self,opt):
        if(opt==6):
            print("Liquidacion honorario");
        else:
           self.getSucesor().request(opt)    

class ManejadorDefault(Manejador):
    def request(self,opt):
        print("Opcion no valida");

manejadores=[0,0,0,0,0,0,0,0];
manejadores[0]=Manejadorbasico(Manejador);
manejadores[1]=ManejadorCatedra(Manejador);
manejadores[2]=Manejadorhc(Manejador);
manejadores[3]=Manejadormto(Manejador);
manejadores[4]=Manejadortco(Manejador);
manejadores[5]=ManejadorHonorarios(Manejador);
manejadores[6]=ManejadorDefault(Manejador);

for i in range(6):
    manejadores[i].setSucesor(manejadores[i+1]);
manejadores[0].request(90);


    
