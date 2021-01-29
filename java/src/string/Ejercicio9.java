package string;

public class Ejercicio9 {

	public final static String VOCALES = "aeiou";
	
	public static void main(String[] args) {
		System.out.println(reordenarFrase("Curso de programAcion"));
		
	}
	
	public static String reordenarFrase(String fraseEntrada) {
		
		fraseEntrada=fraseEntrada.replace(" ", "").toLowerCase();
		StringBuilder vocales = new StringBuilder();
		StringBuilder consonantes = new StringBuilder();
		
		for(int i=0; i<fraseEntrada.length(); i++) {
			char c = fraseEntrada.charAt(i);
			
			if(VOCALES.indexOf(c)>=0) {
				vocales.append(c);
			}else {
				consonantes.append(c);
			}
		}
		
		return consonantes.append(vocales.toString()).toString();				
				
	}
		
}
