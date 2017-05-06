/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package chain.of.responasabolity;

/**
 *
 * @author Estudiantes
 */
public class manejadortco extends Manejador{

    @Override
    public void handlerRequest(int opt) {
        if(opt == 3){
            System.out.println("Liquidacion tco");
        }else{
            successor.handlerRequest(opt);
        }    }
    
}
