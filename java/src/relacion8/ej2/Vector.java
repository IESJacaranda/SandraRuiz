package relacion8.ej2;

/**
 * Este ejercicio utiliza el método formateaAString de la clase Matriz del paquete matrices.ejemplo
 */

public class Vector {
	
	public static int[] desplazarElementosDerecha(int[] vector) {
		
		int ultimoValor = vector[vector.length-1];
		for(int i=vector.length-1; i>0; i--) {
			vector[i]=vector[i-1];
			
		}
		vector[0]=ultimoValor;
		return vector;
		
	}
	
	public static int[] desplazarElementosIzquierda(int[] vector) {
		
		
		return vector;
		
	}
}
