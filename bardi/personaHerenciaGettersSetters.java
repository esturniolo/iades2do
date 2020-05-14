/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package persona;

/**
 *
 * @author eas
 */
public class Persona {
    public static void main(String[] args){
        
    } 
    String Nombre;
    String Apellido;
    Integer DNI;
    Boolean Sexo;
    /**
     * @param args the command line arguments
     */
class Profesional extends Persona{
   String Titulo;
   String Titulacion;
    }


public String getNombre(){
    return Nombre;
}

public String getApellido(){
    return Apellido;
}

public int getDNI(){
    return DNI;
}

public boolean getSexo(){
    return Sexo;
}

public void setNombre(String Nombre){
    this.Nombre = Nombre;
    }

public void setApellido(String Apellido){
    this.Apellido = Apellido;
    }

public void setDNI(int DNI){
    this.DNI = DNI;
    }

public void setSexo(boolean Sexo){
    this.Sexo = Sexo;
    }

}

