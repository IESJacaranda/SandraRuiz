package poo4;

import java.util.Scanner;

public class Main {


		
	public final static String MENU="1. Sumar complejos \n"+
							 "2. Restar complejos \n"+
							 "3. Comparar complejos \n"+
							 "4. Salir";
	
	

	public static void main(String[] args) {
		gestionarInterfaz();
	}
	
	
	static Scanner teclado = new Scanner(System.in);
	
	
	/**
	 * Este método se utiliza para gestionar la interfaz de la calculadora
	 * de números complejos
	 */
	public static void gestionarInterfaz() {
		
		int opcion=0;
		
		while(opcion!=4) {
			showMenu();
			opcion = Integer.parseInt(teclado.nextLine());
			try {
				switch(opcion) {
				
				case 1:
					Complejo c1 = pedirNumeroComplejo();
					Complejo c2 = pedirNumeroComplejo();
					System.out.println(c1.suma(c2));
					break;
				case 2:
					c1 = pedirNumeroComplejo();
					c2 = pedirNumeroComplejo();
					System.out.println(c1.resta(c2));
					break;
				case 3:
					c1 = pedirNumeroComplejo();
					c2 = pedirNumeroComplejo();
					if(c1.equals(c2)) {
						System.out.println("Los números son iguales");
					}else {
						System.out.println("Los números comparados son diferentes");
					}
					break;
				default: 
					break;
					
				}
			}catch(Exception ex) {
				System.out.println(ex.getMessage());
			}
			
		}
	
	}
	
	
	public static Complejo pedirNumeroComplejo() throws Exception {
		Complejo numero = new Complejo();
		try {
			System.out.println("Introduzca la parte real del número complejo: ");
			numero.setReal(Double.parseDouble(teclado.nextLine()));
			
			System.out.println("Introduzca la parte imaginaria del número complejo: ");
			numero.setImaginaria(Double.parseDouble(teclado.nextLine()));
		}catch(Exception ex) {
			Exception nueva = new Exception("El valor introducido no se corresponde con un número válido");
			throw nueva;
		}
		
		return numero;
	}
	
	
	public static void showMenu() {
		System.out.println(MENU);
	}
		
}
