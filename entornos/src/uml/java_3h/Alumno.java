package uml.java_3h;

import java.util.ArrayList;

public class Alumno {
	private String dni;
	private String nombre;
	private String direccion;
	private String beca;

	private ArrayList<Grupo> grupos = new ArrayList();
	
	public Alumno(String dni, String nombre, String direccion, String beca) {
		this.dni=dni;
		this.nombre=nombre;
		this.direccion=direccion;
		this.beca=beca;
	}
	
	public void asignarAlumnos(Grupo grupo) {
		this.grupos.add(grupo);
	}

}
