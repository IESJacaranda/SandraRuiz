package examen.febrero.ej1;

import java.util.Scanner;

public class Principal {
	
	public static final String MENU_PRINCIPAL = "1. Consultar número de mensajes\n" + 
									"2. Consultar mensaje\n" + 
									"3. Añadir mensaje\n" + 
									"4. Borrar todos los mensajes\n" + 
									"5. Salir";
	
	public static final String MENU_MENSAJES= "1. Mensaje número 1\n" +
											"2. Mensaje número 2\n" +
											"3. Mensaje número 3\n";
	
	private static Scanner teclado = new Scanner(System.in);
	
	
	public static void main(String[] args) {
		showMainMenu();
		int opcionMenuPrincipal = Integer.parseInt(teclado.nextLine());
		
		Contestador contestador = new Contestador();
		contestador.setMensaje1("mensaje1");
		contestador.setMensaje2("mensaje2");
		contestador.setMensaje3("mensaje3");
		
		while(opcionMenuPrincipal!=5) {
		
			switch (opcionMenuPrincipal) {
			case 1:
				System.out.println("Existen " + contestador.getNumeroMensajes()+ " mensajes");
				break;
			case 2:
				subMenu(contestador);
				break;
			case 3:
				System.out.println("Introduzca el mensaje que quiere guardar");
				String mensaje = teclado.nextLine();
				try {
					contestador.addMensaje(mensaje);
				} catch (Exception e) {
					System.out.println(e.getMessage());
				}
				break;
			case 4:
				contestador.borrarTodosLosMensajes();
				break;
			default:
				break;
			}
			showMainMenu();
			opcionMenuPrincipal = Integer.parseInt(teclado.nextLine()); 
		}
	}

	public static final String OPCIONES_MENSAJES = "1. Oír \n"+"2. Borrar \n";
	
	public static void subMenu(Contestador contestador) {
		System.out.println("¿Qué mensaje desea consultar?");
		System.out.println(MENU_MENSAJES);
		int numMensaje = Integer.parseInt(teclado.nextLine());
		int opcion = 0;
		
		
		if(numMensaje > 0 && numMensaje <=3) {
			System.out.println(OPCIONES_MENSAJES);
			switch (numMensaje) {
			case 1:
				opcion = Integer.parseInt(teclado.nextLine());
				if(opcion==1) {
					try {
						System.out.println(contestador.getMensaje1());
					} catch (Exception e) {
						System.out.println(e.getMessage());
					}
				}else if(opcion==2) {
					contestador.borrarMensaje1();
				}
				break;
			case 2:
				break;
			case 3:
				break;
			}
		
		}else {
			System.out.println("Opción no válida");
		}
	}
	
	public static void showMainMenu() {
		System.out.println(MENU_PRINCIPAL);
		
	}
}
