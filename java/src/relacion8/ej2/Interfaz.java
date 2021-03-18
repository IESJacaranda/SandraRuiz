package relacion8.ej2;

import java.util.Scanner;

import matrices.ejemplo.Matriz;


/**
 * Este ejercicio utiliza el método formateaAString de la clase Matriz del paquete matrices.ejemplo
 */


public class Interfaz {

	
	public final static int MAX_ITERACIONES = 10;
	

	public static void introducirElementos() {
	
		Scanner teclado = new Scanner(System.in);
	
		int[] vector = new int[MAX_ITERACIONES];
		
		for(int i=0; i<MAX_ITERACIONES; i++) {
			System.out.println("Introduce el número en la posición "+ (i+1) + "/" + MAX_ITERACIONES);
			vector[i]=Integer.parseInt(teclado.nextLine());
		}
		System.out.println("Vector original:  "+Matriz.formateaAString(vector));
		System.out.println("Vector después de desplazar a la derecha: "+Matriz.formateaAString(Vector.desplazarElementosDerecha(vector)));
		System.out.println("Vector después de desplazar a la izquierda: "+Matriz.formateaAString(Vector.desplazarElementosIzquierda(vector)));
	
	
	}
}
