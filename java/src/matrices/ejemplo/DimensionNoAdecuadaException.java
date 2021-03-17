package matrices.ejemplo;

public class DimensionNoAdecuadaException extends Exception {
	
	public DimensionNoAdecuadaException() {
		super("Las matrices no tienen las mismas dimensiones");
		
	}
}
