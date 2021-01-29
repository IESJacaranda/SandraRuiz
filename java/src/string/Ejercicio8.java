package string;

public class Ejercicio8 {
	
	public static void main(String[] args) {
		
		System.out.println(contarVocales("Una Frase Con Mayusculas"));
		System.out.println(contarVocales("Abaco"));
		System.out.println(contarVocales("Murcielago"));		
	}
	
	/**
	 * Cuenta las vocales distintas dentro de una cadena de texto
	 * @param frase Cadena a comprobar
	 * @return Número de vocales distintas
	 */
	public static int contarVocales(String frase) {
		frase = frase.toLowerCase();
		String vocalesDistintas = "";
		String vocales = "aeiou";
		
		
		for (int i=0;i<frase.length(); i++) {
			char c = frase.charAt(i);
			
			if(vocalesDistintas.indexOf(c)<0 && vocales.indexOf(c)>=0) {
				vocalesDistintas+=c;				
			}
		}
		return vocalesDistintas.length();
			
	}
}
