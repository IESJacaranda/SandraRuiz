package string;

public class Ejercicio06 {
	
	public static void main(String[] args) {
		
		System.out.println(buscaPalabra("shybaoxlna", "hola"));
		
	}
	
	public static boolean buscaPalabra(String cadenaCompleta, String oculta) {
		
		int indiceOculta = 0;
		
		if(cadenaCompleta.length()>=oculta.length()) {
			
			for(int i=0; i<cadenaCompleta.length(); i++) {
				if(indiceOculta<oculta.length() 
						&& cadenaCompleta.toLowerCase().charAt(i)==oculta.toLowerCase().charAt(indiceOculta)) {
					
					indiceOculta++;
				}
				
			}
		}
		
		return indiceOculta==oculta.length();
	}

}
