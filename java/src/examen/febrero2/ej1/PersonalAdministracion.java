package examen.febrero2.ej1;

public class PersonalAdministracion extends Empleado {

	private String ubicacion;
	private String telefono;
	private String areaResponsabilidad;
	
	public PersonalAdministracion() {}
	
	public PersonalAdministracion(String ubicacion, String telefono, String areaResponsalibidad) {
		this.ubicacion=ubicacion;
		this.telefono=telefono;
		this.areaResponsabilidad=areaResponsabilidad;
	}
	
	/*
	 * Este método comprueba que el área de responsabilidad sea correcta y,
	 * de lo contrario, lanza una excepción
	 */
	public void comprobarAreaResponsabilidad() throws Exception {
		if(areaResponsabilidad.length()>0 
				&& areaResponsabilidad.contains("gestión del alumnado") 
				|| areaResponsabilidad.contains("profesorado")) {
			this.areaResponsabilidad=areaResponsabilidad;
			
		}else {
			throw new Exception("El área de responsabilidad no es correcta");
		}
			
	}
	
	
	public String getUbicacion() {
		return ubicacion;
	}
	public void setUbicacion(String ubicacion) {
		this.ubicacion = ubicacion;
	}
	public String getTelefono() {
		return telefono;
	}
	public void setTelefono(String telefono) {
		this.telefono = telefono;
	}
	public String getAreaResponsabilidad() {
		return areaResponsabilidad;
	}
	public void setAreaResponsabilidad(String areaResponsabilidad) {
		this.areaResponsabilidad = areaResponsabilidad;
	}

	@Override
	public String toString() {
		return "El empleado forma parte del personal de Administracion de centro, su ubicación " + this.ubicacion + ", su teléfono es " + this.telefono + " y su área de responsabilidad es "
				+ this.areaResponsabilidad + ".";
	}
	
	
}
