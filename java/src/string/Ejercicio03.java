package string;

public class Ejercicio03 {

	public static int lowCaseInString(String cadena) {
		int contador = 0;
		
		for(int i=0; i<cadena.length(); i++) {
			if(Character.isUpperCase(cadena.charAt(i))) {
				contador++;
			}
		}
		
		return contador;
	}
}
