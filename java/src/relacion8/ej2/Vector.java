package relacion8.ej2;

import java.util.Scanner;

/**
 * Este ejercicio utiliza el método formateaAString de la clase Matriz del paquete matrices.ejemplo
 */

	
public class Vector {
	
	
	/**
	 * Este método recibe un vector y desplaza sus elementos a la derecha, 
	 * poniendo el último elemento en primer lugar
	 * @param vector
	 * @return vector desplazado a la derecha
	 */
	public static int[] desplazarElementosDerecha(int[] vector) {
		
		int ultimoValor = vector[vector.length-1];
		for(int i=vector.length-1; i>0; i--) {
			vector[i]=vector[i-1];
			
		}
		vector[0]=ultimoValor;
		return vector;
		
	}
	/**
	 * Este método recibe un vector y desplaza sus elementos a la izquierda, 
	 * poniendo el primer elemento en último lugar
	 * @param vector
	 * @return vector desplazado a la izquierda
	 */
	public static int[] desplazarElementosIzquierda(int[] vector) {
		
		int ultimoValor = vector[0];
		for(int i=0; i<vector.length-1; i++) {
			vector[i]=vector[i+1];
			
		}
		vector[vector.length-1]=ultimoValor;
		return vector;
		
		
		
	}
	
	
}
