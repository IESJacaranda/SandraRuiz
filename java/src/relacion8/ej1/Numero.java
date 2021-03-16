package relacion8.ej1;

import java.util.Scanner;

public class Numero {

	public static void main(String[] args) {
		
		ordenarALaInversa();
		
		
	}
	/** Este método ordena una lista de 10 números enteros
	 * pedidos por teclado en orden inverso al orden de 
	 * introducción
	 */
	public static void ordenarALaInversa() {
		
		
		int[] lista = new int[10];
		
		Scanner teclado = new Scanner(System.in);
		
		for(int i=0; i<lista.length;i++) {
			System.out.println("Introduce un número entero: ");
			lista[i]=Integer.parseInt(teclado.nextLine());
		}
			
		for(int i=9; i>=0;i--) {
			System.out.println(lista[i]);	
		}	
		
	}
		
}
