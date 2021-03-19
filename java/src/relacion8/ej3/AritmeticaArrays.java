package relacion8.ej3;

import java.util.Scanner;

import matrices.ejemplo.Matriz;

public class AritmeticaArrays {

	public static void main(String[] args) {
		AritmeticaArrays aa = new AritmeticaArrays();
		aa.gui();
	}
		//public static String pedirNumeros() {
	
	
	public void gui() {
		Scanner teclado = new Scanner(System.in);
		int numero = -1;
		
		while(numero!=0) {
			System.out.println("Introduce un número entero entre 1 y 1000");
			numero = Integer.parseInt(teclado.nextLine());
			if(numero > 0 && numero <1001) {
				suma+=numero;
				contarDigitos(String.valueOf(numero));
				
			}
		}
		//Imprimimos info
		obtenerEstadisticas();
	}
	
	public void obtenerEstadisticas() {
		System.out.println("La media total de los números introducidos es: "+calcularMedia());
		System.out.println("El dígito en el que han acabado más números es el: "+ getMaxOcurrences());
		System.out.println("la frecuencia de aparición de cada dígito es: " + getCounterList());
		System.out.println("NO OCURRENCIAS: ");
		System.out.println(getNoOcurrences());
	}	
	
	private int[] contadorDigitos = new int[10];
	
	private int suma = 0;
	
	public AritmeticaArrays() {
		
	}
	
	/**
	 * Este método 
	 * @param numero
	 */
	public void contarDigitos(String numero) {
		
		if(numero!=null && !numero.isBlank()) {
			int number= Integer.valueOf(numero.substring(numero.length()-1));
			contadorDigitos[number]=contadorDigitos[number]+1;
		}
	}
	
	public String getCounterList() {
		return Matriz.formateaAString(contadorDigitos);
	}
	
	public int sumarNumeros(String numero) {
		
		if(numero!=null && !numero.isBlank()) {
			suma+=Integer.valueOf(numero);
		}
		return suma;
	}
	
	public double calcularMedia() {
		
		int totalDigitos = 0;
		
		for(int i=0; i<contadorDigitos.length; i++) {
			totalDigitos+=contadorDigitos[i];
				
		}
		return suma/totalDigitos;
			
	}
	
	public String getNoOcurrences() {
		
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<contadorDigitos.length; i++) {
			if(contadorDigitos[i]==0) {
				sb.append("No se ha introducido ningún número terminado en "+i+"\n");
			}
		}
		return sb.toString();
		
	}
	
	public String getOcurrences() {
		
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<contadorDigitos.length; i++) {
			sb.append("Ha habido " + contadorDigitos[i]+" ocurrencias de números terminados en "+ i+"\n");
		}
		return sb.toString();
		
	}
	
	public String getMaxOcurrences() {
		
		int max = contadorDigitos[0];
		int posicionDelMax = 0;
		for(int i=0; i<contadorDigitos.length; i++) {
			if(max < contadorDigitos[i]) {
				max = contadorDigitos[i];
				posicionDelMax = i;
			}
		}
		return ""+posicionDelMax;
	}
	
	

	
}
