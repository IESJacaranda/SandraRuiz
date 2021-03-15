package uml.java_3h;

public class Matricula {
	private String calificacion;
	
	public Alumno alumno;
	public Grupo grupo;
	
	
	public Matricula(String calificacion, Alumno alumno, Grupo grupo) {
		this.calificacion = calificacion;
		this.alumno = alumno;
		this.grupo = grupo;
	}
	
}
