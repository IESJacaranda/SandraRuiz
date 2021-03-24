package relacion8.ej4;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		gui();

	}
	
	public static void gui() {
		int day, month, year;
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduce el día de la fecha:");
		day = Integer.parseInt(teclado.nextLine());
		
		System.out.println("Introduce el mes de la fecha:");
		month = Integer.parseInt(teclado.nextLine());
		
		System.out.println("Introduce el año de la fecha:");
		year = Integer.parseInt(teclado.nextLine());
		
		
		try {
			Fecha fecha = new Fecha(day,month,year);
			System.out.println(fecha.pasarAFormatoLargo());
			
		} catch (FechaNoValidaException e) { // podría ponerse la clase padre (Exception e)
			System.out.println(e.getMessage());
		}
		
		
		/* 
		 Ejemplo con varias excepciones y llamada a clase padre
		
		try {
			Fecha fecha = new Fecha(day,month,year);
			System.out.println(fecha.pasarAFormatoLargo());
			
		} catch (NullPointerException e) { 
			System.out.println("Se ha producido un nullPointer");
		} catch (FechaNoValidaException e) {
			System.out.println(e.getMessage());
		} catch (Exception e) { //Este no podría ir nunca en primer lugar, porque siempre saldría él antes que el NullPointerException, pq ya maneja dicha excepcion.
			System.out.println("Se ha producido una excepción genérica");
		} finally {
			System.out.println("Hasta luego!");
		
		//El catch se pasa si hay una excepcion, pero el finally siempre se ejecuta, aunque no se lance la excepción.
		 
		 */
	}

}
