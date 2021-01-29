package string;

public class Ejercicio04 {

	public static int lowCaseInString(String cadena) {
		int contador = 0;
		
		for(int i=0; i<cadena.length(); i++) {
			if(Character.isDigit(cadena.charAt(i))) {
				contador++;
			}
		}
		
		return contador;
	}
}
