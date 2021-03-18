package relacion8.ej3;

import java.util.Scanner;

public class AritmeticaArrays {

	private int[] contadorDigitos = new int[10];
	
	public AritmeticaArrays() {
		
	}
	
	public void contarDigitos(String numero) {
		if(numero!=null && !numero.isBlank()) {
			contadorDigitos[Integer.valueOf(numero.charAt(numero.length()-1)).intValue()]=
					contadorDigitos[Integer.valueOf(numero.charAt(numero.length()-1))]+1;
		}
	}
	
	
	/*public static void pedirNumeros() {
		Scanner teclado = new Scanner(System.in);
		
		int[] vector =  new int[10];
		

		System.out.println("Desea continuar? (s/n)");
		
		while(teclado.nextLine()!="n") {
			System.out.println("Introduzca un número entero entre 1 y 1000: ");
			for(i=0; i<vector.length; i++ ) {
				vector[i]=Integer.parseInt(teclado.nextLine());
				
			}
		}*/
	
	/*public static double calcularMedia(int[] vector) {
		
		int suma = 0;
		double media = 0.0;
		
		
		if(vector!=null && vector.length>=1) {
			
			for(int i=0; i<vector.length; i++) {
				suma = suma + vector[i];
				
			}
		}else {
			
		}
		return media;
			
	}*/
	
	

	
	
}
