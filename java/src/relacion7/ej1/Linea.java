package relacion7.ej1;

public class Linea {

	private Punto puntoA;
	private Punto puntoB;
	
	
	/**
	 * Constructor por defecto
	 */
	public Linea() {
		this.puntoA = new Punto(0.0, 0.0);
		this.puntoB = new Punto(); //se puede poner así pq el valor por defecto de Punto va a ser 0 
	}
	
	
	/**
	 * Constructor con argumentos. Recibe dos objetos de la clase Punto
	 * y los asigna a las propiedades de la clase
	 * @param pA Punto A
	 * @param pB Punto B
	 */
	public Linea(Punto pA, Punto pB) {
		this.puntoA = pA;
		this.puntoB = pB;
	}

	
	
	public Punto getPuntoA() {
		return puntoA;
	}


	public void setPuntoA(Punto puntoA) {
		this.puntoA = puntoA;
	}


	public Punto getPuntoB() {
		return puntoB;
	}


	public void setPuntoB(Punto puntoB) {
		this.puntoB = puntoB;
	}

	
	public void moverArriba(double distancia) {
		this.puntoA.moverArriba(distancia);
		this.puntoB.moverArriba(distancia);
	}
	
	public void moverAbajo(double distancia) {
		this.puntoA.moverAbajo(distancia);
		this.puntoB.moverAbajo(distancia);
	}
	
	public void moverDerecha(double distancia) {
		this.puntoA.moverDerecha(distancia);
		this.puntoB.moverDerecha(distancia);
	}
	
	public void moverIzquierda(double distancia) {
		this.puntoA.moverIzquierda(distancia);
		this.puntoB.moverIzquierda(distancia);
	}
	
	
	@Override
	public boolean equals(Object obj) {
		boolean sonIguales = false;
		
		if(this==obj) { //compara el objeto consigo mismo, es decir, que ocupan el mismo espacio de memoria
			sonIguales = true;
		}else if(obj!=null && obj instanceof Linea 
				&& ((Linea)obj).getPuntoA().equals(this.puntoA) 
				&& ((Linea)obj).getPuntoB().equals(this.puntoB)) {
				sonIguales = true;	
		}
		return sonIguales;
	}

	@Override
	public String toString() {
		return "["+ this.getPuntoA()+", "+this.getPuntoB()+"]";
	}


	
	
}
