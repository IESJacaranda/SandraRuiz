package herencia.ejemplo.inventado;

public class Bovido extends Animal {

	public Bovido() {
		super();
	}
	
	@Override
	public void vivirLugar() {
		System.out.println("Vive en una granja");
	}
	
	@Override
	public void comer() {
		System.out.println("Es herbívoro");
	}
	
}
