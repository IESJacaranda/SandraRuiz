package java.com.edu;

public class Main {

	public static void main(String[] args) {
		
		
		Persona joseManuel = new Persona();
		
		Persona fran = new Persona();
		
		Persona x = joseManuel;
		
		Persona sandra = new Persona("Sandra", 1.50);
		sandra.setNombre("Sandra");
		
		System.out.println(sandra);
		
		
			
			
		}
		
		//StringBuilder stringBuilder;
		
		//System.out.println(joseManuel); //imprime el objeto y su id en memoria
		//System.out.println(fran); //imprime el objeto y su id en memoria, que son distintos al de joseManuel.
		//System.out.println(x); //imprime el mismo objeto e id de joseManuel
		
		//System.out.println(joseManuel);
		
		//joseManuel.setNombre("José Manuel");
		//joseManuel.getEdad();
		//joseManuel.altura=1.7;
		
		//System.out.println(joseManuel.getEdad()); 
		//System.out.println(joseManuel.altura); //imprime 1.7
		
	//}

}
