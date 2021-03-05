package examen.febrero2.ej1;

public class Profesor extends Empleado {
	private String departamento;
	private String modulo;
	private String curso;
	
	
	/*
	 * Constructor vacío
	 */
	
	public Profesor() {}
	
	/*
	 * Constructor
	 */
	
	public Profesor(String departamento, String modulo, String curso) {
		this.departamento=departamento;
		this.modulo=modulo;
		this.curso=curso;
	}
	
	
	
	public String getDepartamento() {
		return departamento;
	}
	public void setDepartamento(String departamento) {
		this.departamento = departamento;
	}
	public String getModulo() {
		return modulo;
	}
	public void setModulo(String modulo) {
		this.modulo = modulo;
	}
	public String getCurso() {
		return curso;
	}
	public void setCurso(String curso) {
		this.curso = curso;
	}

	@Override
	public String toString() {
		return "Es un/a profesor/a del Departamento de " + this.departamento + " y da clases en el módulo " + this.modulo + ", en el curso " + this.curso + ".";
	}
	
	
	
}
