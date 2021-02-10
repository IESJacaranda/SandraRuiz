package java.com.edu;

public class Persona {

	private String nombre;
	private int edad;
	public double altura;
	int peso;

	//Constructor vacío
	public Persona( ) {
		
	}
	
	//Constructor con argumentos
	public Persona(String nombre, double altura) {
		this.nombre=nombre;
		this.altura=altura;
		
	}
	
	
	//Lo habitual es hacer todos private y para eso se utilizan dos métodos 
	//get y set
	//que hacen que estén disponibles para otra clase:
	
	
	public int getEdad() {
		return edad;
	}
	
	//o
	
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	
}
