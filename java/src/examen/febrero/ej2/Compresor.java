package examen.febrero.ej2;

/**
 * Clase de utilidad para comprimir y descomprimir cadenas de caracteres
 * @author sandra
 *
 */
public class Compresor {

	/**
	 * Este método comprime una cadena de caracteres	
	 * @param cadena a comprimir
	 * @return cadena comprimida
	 */
	public String encriptar(String cadena) {
		
		StringBuilder sb = new StringBuilder();
		
		if(cadena!=null && cadena.length()>0) {
			int counter = 1;
			
			char a = cadena.charAt(0);
			
			for(int i=0; i<cadena.length();i++) {
				if(a == cadena.charAt(i)) {
					counter++;
				}else if(i==cadena.length()-1) {
					sb.append(a).append(counter);
				}else {
					sb.append(a).append(counter);
					a = cadena.charAt(i);
					counter = 1;
				}
			}
		
		}
				
		return sb.toString();
	}
	
	
	public String desencriptar(String cadena) {
		
		StringBuilder resultado = new StringBuilder();
		
		if(cadena!=null && !cadena.isEmpty() && cadena.length()>=2) {
			
			char caracterARepetir = cadena.charAt(0);
			String veces = "";
			
			for(int i=1; i<cadena.length();i++) {
				
				if(Character.isDigit(cadena.charAt(i))) {
					veces+=cadena.charAt(i);
				}else {
					resultado.append(caracterARepetir, veces));
					veces = "";
					caracterARepetir=cadena.charAt(i);
				}
			}
			resultado 
		}
		
		return resultado.toString();
	}
	
	
	private String repetir(char caracter, String veces) {
		StringBuilder sb = new StringBuilder();
		int vecesNum = Integer.parseInt(veces);
		for(int j=0; j<vecesNum; j++) {
			sb.append(caracter);
		}
		return sb.toString();
	}
}
