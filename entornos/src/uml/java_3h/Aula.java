package uml.java_3h;

import java.util.ArrayList;

public class Aula {
	private String id;
	private int capacidad;
	
	private ArrayList<Asignada> asignadas = new ArrayList();

	public Aula(String id, int capacidad) {
		super();
		this.id = id;
		this.capacidad = capacidad;
	}
	
	public void asignar(Asignada asignada) {
		this.asignadas.add(asignada);
	}
}
