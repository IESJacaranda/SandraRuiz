package interf.ejemplo.propio;

public class Quiroptero implements IMamifero {
	
	private int peso;
	private int numeroMamas;
	private int tiempoGestacion;
	
	
	public Quiroptero (int peso, int numeroMamas, int tiempoGestacion) {
		this.peso = peso;
		this.numeroMamas = numeroMamas;
		this.tiempoGestacion = tiempoGestacion;
	}
	
	public int getPeso() {
		return this.peso;
	}
	
	@Override
	public int getNumeroMamas() {
		// TODO Auto-generated method stub
		return this.numeroMamas;
	}

	@Override
	public int getTiempoGestacion() {
		// TODO Auto-generated method stub
		return this.tiempoGestacion;
	}

}
