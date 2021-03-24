package interf.ejemplo.propio;

public class Sphenisciforme implements IAnimalMarino {
	
	private int peso;
	private String tipoAlimentacion;
	private boolean tieneBranquias = false;
	
	public Sphenisciforme(int peso, String tipoAlimentacion) {
		this.peso = peso;
		this.tipoAlimentacion = tipoAlimentacion;
	}
	
	@Override
	public double getPeso() {
		// TODO Auto-generated method stub
		return this.peso;
	}

	@Override
	public String tipoAlimentacion() {
		// TODO Auto-generated method stub
		return this.tipoAlimentacion;
	}

	@Override
	public boolean tieneBranquias() {
		// TODO Auto-generated method stub
		return false;
	}

	

}
