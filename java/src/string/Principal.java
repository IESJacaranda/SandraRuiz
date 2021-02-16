package string;

public class Principal {

	public static void main(String[] args) {
		
		Frase frase = new Frase("He estudiado mucho");
		System.out.println(frase.contarPalabras());

		Frase frase2 = new Frase("    He     estudiado    mucho              ");
		System.out.println(frase2.contarPalabras());
		
		/**
		 * indexOf nos devuelve posición en cadena de texto.
		 * En línea 20 da posición 8.
		 * En línea 21 da posición -1, ya que no lo encuentra.
		 * Línea 22 devuelve las 9 de la mañana (recorda desde posicion 3).
		 */
		//String texto = "Son las 9 de la mañana";
		//System.out.println(texto.indexOf('9'));
		//System.out.println(texto.indexOf('0'));
		//System.out.println(texto.substring(3));
	}

}
