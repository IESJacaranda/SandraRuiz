package uml.java_3h;

import java.util.ArrayList;

public class Grupo {

	private String id;
	private String tipo;
	
	public Asignatura asignatura;
	
	private ArrayList<Asignada> aulas = new ArrayList();
	
	private ArrayList<Alumno> alumnos = new ArrayList();
	
	private ArrayList<Profesor> profesores = new ArrayList();
	
	public Grupo(String id, String tipo, Asignatura asignatura) {
		this.id=id;
		this.tipo=tipo;
		this.asignatura=asignatura;
	}
	
	public void asignarAulas(Asignada aula) {
		this.aulas.add(aula);
	}
	
	public void asignarAlumnos(Alumno alumno) {
		this.alumnos.add(alumno);
	}
	
	public void asignarProfesores(Profesor profesor) {
		this.profesores.add(profesor);
	}
}
