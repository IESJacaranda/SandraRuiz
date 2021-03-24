package interf.ejemplo.propio;

public class Cetaceo implements IAnimalMarino, IMamifero {

	private int peso;
	private int numeroMamas;
	private int tiempoGestacion;
	private String tipoAlimentacion;
	
	
	public Cetaceo(int peso, int numeroMamas, int tiempoGestacion, String tipoAlimentacion) {
		this.peso = peso;
		this.numeroMamas = numeroMamas;
		this.tiempoGestacion = tiempoGestacion;
		this.tipoAlimentacion = tipoAlimentacion;
	}
	
	
	@Override
	public int getNumeroMamas() {
		return this.numeroMamas;
	}

	@Override
	public int getTiempoGestacion() {
		return this.tiempoGestacion;
	}

	@Override
	public double getPeso() {
		return this.peso;
	}

	@Override
	public String tipoAlimentacion() {
		return this.tipoAlimentacion;
	}

	@Override
	public boolean tieneBranquias() {
		return false;
	}



}
