package string;

//Ejercicio5, palíndromos

public class Ejercicio5 {
	
	public static void main(String[] args) {
				
		System.out.println(palyndrome("CadeNa de texto OtxEted AneDac"));
		System.out.println(palyndrome("CadeNa de textoneDac"));
						
	}
	
	
	public static boolean palyndrome(String cadena) {
		boolean isPalyndrome=false;
		cadena=cadena.replace(" ", "").toLowerCase();
		String inverse = "";
		for(int i=0; i<cadena.length(); i++) {
			inverse = cadena.charAt(i)+inverse;
		}
		isPalyndrome = inverse.contentEquals(cadena);
		
		return isPalyndrome;
	}
	
	
}