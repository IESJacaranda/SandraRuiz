package interf.ejemplo.propio;

public class Murcielago extends Quiroptero {
	
	private String tipoAlimentacion;
	
	
	public Murcielago(int peso, int numeroMamas, int tiempoGestacion, String tipoAlimentacion) {
		super(peso, numeroMamas, tiempoGestacion);
		this.tipoAlimentacion = tipoAlimentacion;
	}
	
	public String seAlimenta() {
		return this.tipoAlimentacion;
	}
	
}
