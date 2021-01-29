package string;

public class Ejercicio07 {

	public static void main(String[] args) {
		
		System.out.println(reemplazar("Hola, José, ¿cómo estás?, José", "José", "Ramón"));
		
	}
	
	/**
	 * Este método sustituye una palabra por otra en una cadena de texto
	 * @param frase Cadena de texto a modificar
	 * @param palabra Palabra a reemplazar
	 * @param nuevaPalabra Palabra con la que se reemplaza
	 * @return La cadena con el reemplazo
	 */
	
	public static String reemplazar(String frase, String palabra, String nuevaPalabra) {
				
		return frase.replace(palabra, nuevaPalabra);
							
	}
}
