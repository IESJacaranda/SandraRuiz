package string;

public class Ejercicio10 {

	public static void main(String[] args) {
		
		System.out.println(contarPalabras("no me gustan los lichis"));
		System.out.println(contarPalabras("  no me gustan los lichis"));
		System.out.println(contarPalabras("arrrrgggg no me gustan los lichis"));
		System.out.println(contarPalabras("   arrrrgggg         no me   gustan los      lichis "));
		System.out.println(contarPalabras("arrrrgggg no me gustan los lichis   "));
		System.out.println(contarPalabras("   arrrrgggg         no me   gustan los      lichis "));
		
	}
	
	
	/**
	 * Este método recibe un String
	 * Devuelve el número de palabras que contiene
	*/
	public static int contarPalabras(String cadena) {
		int contadorPalabras=0;
		cadena=" " + cadena;
		
		for(int i = 0;i<cadena.length()-1;i++) {
			if (Character.isSpaceChar(cadena.charAt(i)) && Character.isLetter(cadena.charAt(i+1))) {
				
				contadorPalabras=contadorPalabras+1;
			}
		}

		return contadorPalabras;
	
	}
		
}