package string;

import java.util.Scanner;

public class primerEjercicio {

	static Scanner teclado = new Scanner(System.in);
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String cadena;
		char cBuscado, cReemplazar;
				
		System.out.println("Introduce una cadena");
		cadena = teclado.nextLine();
		
		System.out.println("Introduce el caracter que queremos buscar");
		cBuscado = teclado.nextLine().charAt(0);
		
		System.out.println("Introduce el caracter a reemplazar");
		cReemplazar = teclado.nextLine().charAt(0);
		
		cadena = cadena.replace(cBuscado,  cReemplazar);
		if (Character.isUpperCase(cBuscado)) {
			cadena = cadena.replace(Character.toLowerCase(cBuscado),  cReemplazar);
		}else {
			cadena = cadena.replace(Character.toUpperCase(cBuscado),  cReemplazar);
		}
				
		String cadena1 = cadena;
			
		System.out.println(cadena + " y " + cadena1);
		
		System.out.println(cadena == cadena1);
// el == compara el objeto, no su contenido. 
		
// Si el tipo empieza por minúsculas, podemos hacer el ==, sino no. Por ej, con String no podemos hacer ==, sino que usaremos el boolean equals.
		
	
				
		System.out.println(cadena.contentEquals(cadena1));
		
		
	}
	
	public static void main(String2[] args) {
		//TODO Auto-generated method stub
	
			int num = charactersInString("Inmaculada Oalias", 'a');
			System.out.println(num);
	
	}

	public static int charactersInString(String cad, char letra) {
		
		int contador = 0 ;
		for (int i=0;i<cad.length();i++) {
			if (cad.charAt(i)== letra) {
				contador++;
		
			}
		}
		
		return contador;
	}
}




