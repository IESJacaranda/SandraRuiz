package galaxia;

public class Personaje {
	private String nombre;
	private double poderDestructor;
	private Pelicula pelicula;
	private double estatura;
	private String especie;
	private double peso;
	
public Personaje() {}
	
	public Personaje(String nombre, double poderDes, Pelicula pelicula, double estatura, String especie, double peso) {
		
		this.nombre = nombre;
		this.poderDestructor = poderDes;
		this.pelicula = pelicula;
		this.estatura = estatura;
		this.especie = especie;
		this.peso = peso;	
		
	}

	

	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public double getPoderDestructor() {
		return poderDestructor;
	}


	public void setDestruccion(int poderDes) { //el poder de destruccion tiene q ser entre 1-100
		if(poderDes>=1 && poderDes<=100) {
			this.poderDestructor = poderDes;
		}
		
	}
	
	
	@Override
	public String toString() {
		String mensaje = "";
		
		if(this.poderDestructor>this.peso) {
			mensaje = "El personaje se llama "+ this.nombre + ","
					+ " mide " + this.estatura + ","
					+ " pertenece a la especie " + this.especie + ","
					+ " y su poder de destrucción es " + this.poderDestructor +".";
		}
		else if (this.poderDestructor<this.peso) {
			mensaje = "El personaje se llama "+ this.nombre + ","
					+ " mide " +this.estatura + ","
					+ " pertenece a la especie " +this.especie + ","
					+ " y pesa " + this.peso +".";
		}
		
		return mensaje;
	}


	public Pelicula getPelicula() {
		return pelicula;
	}


	public void setPelicula(Pelicula pelicula) {
		this.pelicula = pelicula;
	}


	public double getEstatura() {
		return estatura;
	}


	public void setEstatura(double estatura) {
		this.estatura = estatura;
	}


	public String getEspecie() {
		return especie;
	}


	public void setEspecie(String especie) {
		this.especie = especie;
	}


	public double getPeso() {
		return peso;
	}


	public void setPeso(double peso) {
		this.peso = peso;
	}
	
	
}
