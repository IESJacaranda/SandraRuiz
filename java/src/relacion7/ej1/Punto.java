package relacion7.ej1;

public class Punto {

	private double x;
	private double y;
	
	
	public Punto() {}
	
	public Punto(double x, double y) {
		this.x = x;
		this.y = y;
	}


	public double getX() {
		return x;
	}


	public void setX(double x) {
		this.x = x;
	}


	public double getY() {
		return y;
	}


	public void setY(double y) {
		this.y = y;
	}


	public void moverArriba(double distancia) {
		this.y+=distancia;
	}
	
	public void moverAbajo(double distancia) {
		this.y-=distancia;
	}
	
	public void moverDerecha(double distancia) {
		this.x+=distancia;
	}
	
	public void moverIzquierda(double distancia) {
		this.x-=distancia;
	}
	
	
	
	@Override
	public boolean equals(Object obj) {
		boolean result = false;
		
		if(this==obj) {
			result = true;
		}else if(obj!=null && obj instanceof Punto 
				&& ((Punto)obj).getX()==this.getX() //this.x devolvería el mismo resultado
				&& ((Punto)obj).getY()==this.getY()) {
				result = true;
		}
		return result;
	}

	@Override
	public String toString() {
		return "("+ this.getX()+", "+this.getY()+")";
	}
	
	
}

