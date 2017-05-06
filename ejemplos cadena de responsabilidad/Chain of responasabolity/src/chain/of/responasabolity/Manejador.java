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
public abstract class Manejador {
     Manejador successor;
    
    public abstract void handlerRequest(int opt);

    public Manejador getSuccessor() {
        return successor;
    }

    public void setSuccessor(Manejador successor) {
        this.successor = successor;
    }    
}
