package galaxia;

public class Pelicula {

	private String nombre;
	private int anyoEstreno;
	private Personaje p1;
	private Personaje p2;
	private Personaje p3;
	
	public Pelicula() {}
	
	public Pelicula (String nombre, int yearEstreno, Personaje p1, Personaje p2, Personaje p3) {
		this.nombre = nombre;
		this.anyoEstreno = yearEstreno;
		this.p1 = p1;
		this.p2 = p2;
		this.p3 = p3;
	}
	

	public String compararPelicula(Pelicula pelicula) {
		String mensaje = "";
		if(this.anyoEstreno>pelicula.anyoEstreno) {
			mensaje = "La película '" + this.nombre + "' es posterior a la película '" + pelicula.nombre +"'.";
		}else if(this.anyoEstreno < pelicula.anyoEstreno) {
			mensaje = "La película '" + this.nombre + "' es anterior a la película '" + pelicula.nombre +"'.";
		}else if(this.anyoEstreno==pelicula.anyoEstreno) {
			mensaje = "Ambas películas fueron estrenadas en la misma fecha.";
		}
				
		return mensaje;
	}


	public String obtenerMaximoPoderPelicula() {
		
		return "El poder máximo de la película es: "+this.p1.getPoderDestructor() +", "
													+this.p2.getPoderDestructor() +", "
													+this.p3.getPoderDestructor() +".";
	}


	public String obtenerPoderPelicula() {
		return "El poder de la película es: " + (this.p1.getPoderDestructor()+this.p2.getPoderDestructor()+this.p3.getPoderDestructor()) +".";
	}
	
	
	
	public String toString() {
		
		String posicion=this.getP1().getNombre();
		String P2 = this.getP2().getNombre();
		String P3 = this.getP3().getNombre();
		
	
		if(posicion.compareTo(P2)>=0){
			posicion = P2 + ", " + posicion;
		}else {
			posicion = posicion + ", " + P2;
		}
		if(posicion.compareTo(P3)>=0){
			posicion = P3 + ", " + posicion;
		}else {
			posicion = posicion + ", " + P3;
		}
			
		return this.nombre + " (" + this.anyoEstreno + "), " + posicion +".";
	}
	
	
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getAnyoEstreno() {
		return anyoEstreno;
	}

	public void setAnyoEstreno(int yearEstreno) {
		this.anyoEstreno = yearEstreno;
	}

	public Personaje getP1() {
		return p1;
	}

	public void setP1(Personaje p1) {
		this.p1 = p1;
	}

	public Personaje getP2() {
		return p2;
	}

	public void setP2(Personaje p2) {
		this.p2 = p2;
	}

	public Personaje getP3() {
		return p3;
	}

	public void setP3(Personaje p3) {
		this.p3 = p3;
	}

}