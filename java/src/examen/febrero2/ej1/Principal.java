package examen.febrero2.ej1;

//import java.util.Scanner;

public class Principal {

	//static Scanner teclado = new Scanner(System.in);
	
	public static void main(String[] args) throws Exception {
		
		Empleado javier = new Empleado("Javier Osorio", 30, "hombre", "10-14 de lunes a viernes", "587908", "34564");
		System.out.println(javier.toString());
		javier.comprobarPassword();
		
		javier = new Profesor("Informática", "Programación", "1ºB");
		System.out.println(javier.toString());
		
		Empleado manuela = new Empleado("Manuela Sánchez", 50, "mujer", "9-14 de martes a viernes", "9876323", "ManuEla134");
		System.out.println(manuela.toString());
		
		manuela = new PersonalDireccion("despacho de dirección", "Dirección");
		System.out.println(manuela.toString());
		((PersonalDireccion) manuela).comprobarCompetencias();
		
		Empleado sofia = new Empleado("Sofía García", 42, "mujer", "8-13 de lunes a jueves", "9876997", "98776330MM");
		System.out.println(sofia.toString());
		
		
		PersonalAdministracion jose = new PersonalAdministracion("despacho 16", "954187389", "gestión del alumnado");
		System.out.println(jose.toString());
		jose.comprobarAreaResponsabilidad();

	}
}
