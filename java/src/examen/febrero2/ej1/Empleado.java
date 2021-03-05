package examen.febrero2.ej1;

public class Empleado {

	private String nombre;
	private int edad;
	private String genero;
	private String horario;
	private String codigo;
	private String password;
	
	/*
	 * Constructor vacío
	 */
	public Empleado() {}
	
	
	public Empleado(String nombre, int edad, String genero, String horario, String codigo, String password) {
		this.nombre=nombre;
		this.edad=edad;
		this.genero=genero;
		this.horario=horario;
		this.codigo=codigo;
		this.password=password;
		
	}
	
	/*
	 * Este método recibe la contraseña y comprueba si cumple los requisitos.
	 */
	
	public void comprobarPassword() throws Exception{
		boolean resultado=false;
		if(this.password!=null && password.length()>=10) {
			resultado=true;
		}else {
			throw new Exception("La contraseña no cumple los requisitos");
		}
			
	}
	
	@Override
	public String toString() {
		return "El empleado seleccionado se llama: " + this.nombre + ", tiene " + this.edad + " años, se identifica como " + this.genero + ", su horario es " + this.horario
				+ ", su código de empleado es " + this.codigo + " y su contraseña de acceso al sistema es " + this.password + ".";
	}
	
	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public int getEdad() {
		return edad;
	}


	public void setEdad(int edad) {
		this.edad = edad;
	}


	public String getGenero() {
		return genero;
	}


	public void setGenero(String genero) {
		this.genero = genero;
	}


	public String getHorario() {
		return horario;
	}


	public void setHorario(String horario) {
		this.horario = horario;
	}


	public String getCodigo() {
		return codigo;
	}


	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}


	public String getPassword() {
		return password;
	}


	public void setPassword(String password) {
		this.password = password;
	}


	
	
	
}
