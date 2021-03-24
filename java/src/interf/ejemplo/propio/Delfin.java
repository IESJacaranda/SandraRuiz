package interf.ejemplo.propio;

public class Delfin extends Cetaceo {
	
	private double tiempoSumergido;

	public Delfin(int peso, int numeroMamas, int tiempoGestacion, String tipoAlimentacion, double tiempoSumergido) {
		super(peso, numeroMamas, tiempoGestacion, tipoAlimentacion);
		this.tiempoSumergido = tiempoSumergido;
	}
	
	public int getTiempoSumergido() {
		return this.getTiempoSumergido();
	}
	
}
