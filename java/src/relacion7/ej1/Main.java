package relacion7.ej1;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		/*
		Linea linea = new Linea(new Punto(3,4.5), new Punto(0.3, 4.8));
		System.out.println(linea);
			
		
		Punto puntito1 = new Punto(5.0, 3.0);
		Punto puntito2 = new Punto(4.0, 2.0);
		Punto puntito3 = new Punto(5.0, 3.0);
		Punto puntito4 = new Punto(4.0, 2.0);
		
		System.out.println(puntito1.equals(puntito2));


		
		System.out.println(linea1.equals(linea2));*/
		
	}
	
	public static void pedirDatos(Punto punto) {
			
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduzca la coordenada x: ");
		punto.setX(Double.parseDouble(teclado.nextLine()));
		
		punto.setX(Double.parseDouble(teclado.nextLine()));
		
		System.out.println("Introduzca la coordenada y: ");
		punto.setY(Double.parseDouble(teclado.nextLine()));

	}

}
