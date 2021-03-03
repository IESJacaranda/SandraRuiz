package relacion7.ej3;

public class JarraVaciaException extends Exception {
	
	public JarraVaciaException () {
		super("La jarra está vacía, por lo que no se puede vaciar");
	}
}
