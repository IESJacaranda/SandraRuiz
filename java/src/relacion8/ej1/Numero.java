package relacion8.ej1;

/**
 * Este ejercicio utiliza el método formateaAString de la clase Matriz del paquete matrices.ejemplo
 */
import java.util.Scanner;

public class Numero {

	public static void main(String[] args) {
				
		
	}
	/** Este método pide 10 números enteros y los guarda en
	 * un vector
	 * return vector de 10 números
	 * @throws Exception 
	 */
	public static int[] pedirNumeros() {
			
		int[] vector = new int[10];
		
		Scanner teclado = new Scanner(System.in);
				
		for(int i=0; i<vector.length;i++) {
			System.out.println("Introduce un número entero: ");
			vector[i]=Integer.parseInt(teclado.nextLine());
		}
		
		
		return vector;
	}
			
	/**
	 * Este método recibe un vector y lo devuelve en orden de posiciones
	 * invertidas
	 * @param vector
	 * @return vector de enteros igual que el original en posición invertida
	 */
	public static int[] invertirVector(int[] vector){
		int [] vectorInvertido = new int[vector.length];
		
		for(int i=0; i<vector.length; i++) {
			vectorInvertido[vector.length-1-i]=vector[i];	
		}	
		return vectorInvertido;
		
	}
		
}
