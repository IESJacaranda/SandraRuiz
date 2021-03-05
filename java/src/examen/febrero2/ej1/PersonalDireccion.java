package examen.febrero2.ej1;

public class PersonalDireccion extends Empleado{
	private String ubicacion;
	private String competencias;
	
	
	public PersonalDireccion() {}
	
	public PersonalDireccion(String ubicacion, String competencias) {
		this.ubicacion=ubicacion;
		this.competencias=competencias;
	}
	
	/*
	 * Este método comprueba que las competencias sean correctas y,
	 * de lo contrario, lanza una excepción
	 */
	public void comprobarCompetencias() throws Exception {
		if(competencias.length()>0 
				&& competencias.contains("Secretaría") 
				|| competencias.contains("Jefatura de estudios")
				|| competencias.contains("Dirección")) {
			this.competencias=competencias;
			
		}else {
			throw new Exception("Las competencias no son correctas");
		}
			
	}
	
	
	public String getUbicacion() {
		return ubicacion;
	}

	public void setUbicacion(String ubicacion) {
		this.ubicacion = ubicacion;
	}

	public String getCompetencias() {
		return competencias;
	}

	public void setCompetencias(String competencias) {
		this.competencias = competencias;
	}

	@Override
	public String toString() {
		return "El empleado forma parte del personal de Dirección, su ubicación en el centro es " 
	+ this.ubicacion + " y sus competencias son " 
				+ this.competencias + ".";
	}
	
	
}
