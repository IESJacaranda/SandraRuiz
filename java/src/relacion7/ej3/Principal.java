package relacion7.ej3;

import java.util.Scanner;

public class Principal {

	static Scanner teclado = new Scanner(System.in);
	
	public static void main(String[] args) throws Exception {
		
		interfaz();
		
	}
		
	public static void mostrarMenu() {
		System.out.println("Escoja una opción: "
							+ "\n 1.Llenar jarra"
							+ "\n 2.Vaciar jarra"
							+ "\n 3.Volcar jarra A en B"
							+ "\n 4.Volcar jarra B en A"
							+ "\n 5.Ver estado de las jarras"
							+ "\n 6.Salir");
	}
	
	public static void  seleccionarJarra() {
		System.out.println("Seleccione una jarra:"
							+ "\n 1. Jarra A"
							+ "\n 2. Jarra B");
	}
	
	
	public static void interfaz() {
		
		System.out.println("Capacidad de la jarra A: ");
		Jarra A = new Jarra(Double.parseDouble(teclado.nextLine()));
		
		System.out.println("Capacidad de la jarra B: ");
		Jarra B = new Jarra(Double.parseDouble(teclado.nextLine()));
		
		int opcion1 = 0;
		int opcion2 = 0;
		
		while (opcion1!=6) {
			
			mostrarMenu();
			opcion1 = Integer.parseInt(teclado.nextLine());
			
			
			try {
				switch (opcion1) {
			case 1:
				seleccionarJarra();
				opcion2 = Integer.parseInt(teclado.nextLine());
				
				while (opcion2!=2 && opcion2!=1) {
					seleccionarJarra();
					opcion2 = Integer.parseInt(teclado.nextLine());
				}if (opcion2 == 1) {
					A.llenarJarra();
				}else if (opcion1 == 2) {
					B.llenarJarra();
				}break;
			case 2:
				seleccionarJarra();
				opcion2 = Integer.parseInt(teclado.nextLine());
				
				while (opcion2!=2 && opcion2!=1) {
					seleccionarJarra();
					opcion2 = Integer.parseInt(teclado.nextLine());
				}if (opcion2==1) {
					A.vaciarJarra();
				}else if (opcion2 == 2){
					B.vaciarJarra();
				}break;
			case 3:
				A.volcarJarra(B);
				break;	
			case 4:
				B.volcarJarra(A);
				break;
			case 5:
				System.out.println("Jarra A:");
				System.out.println(A.toString());
				
				System.out.println("Jarra B:");
				System.out.println(B.toString());
				break;
				
			case 6:
				System.out.println("Ha salido del programa.");
			}
			}catch (Exception ex) {
				System.out.println(ex.getMessage());
			}

		}
	}
}
