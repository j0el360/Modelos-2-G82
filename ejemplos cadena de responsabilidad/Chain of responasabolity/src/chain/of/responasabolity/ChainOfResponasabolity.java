/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package chain.of.responasabolity;

import java.util.Scanner;
/**
 *
 * @author Estudiantes
 */
public class ChainOfResponasabolity {

  
    public static void main(String[] args) {
       Scanner leer=new Scanner(System.in);
       
       Manejador manejadores[]=new Manejador[7];
       manejadores[6]=new manejadorDefault();
       manejadores[5]=new manejadorhonorarios();
       manejadores[4]=new manejadorhc();
       manejadores[3]=new manejadormto();
       manejadores[2]=new manejadortco();
       manejadores[1]=new manejadorcatedra();
       manejadores[0]=new manejadorbasico();
       
       for(int i=0;i<manejadores.length-1;i++){
           manejadores[i].setSuccessor(manejadores[i+1]);
       }
       System.out.println("ingrese un entero: ");
       int opt =  leer.nextInt();
        
        manejadores[0].handlerRequest(opt);
    }
    
}
