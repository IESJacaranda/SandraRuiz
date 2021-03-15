package uml.java_3h;

import java.util.ArrayList;

public class Departamento {
	
	private String id;
	private String nombre;
	
	private Profesor jefe;
	
	private ArrayList<Profesor> miembros = new ArrayList();
	
	public Departamento(String id, String nombre, Profesor jefe) {
		this.id=id;
		this.nombre=nombre;
		this.jefe=jefe;
	}
	
	public void asignarMiembros(Profesor profesor) {
		this.miembros.add(profesor);
	}
}
