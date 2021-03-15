package uml.java_3h;

import java.util.ArrayList;

public class Asignatura {

	private String id;
	private String nombre;
	private int creditos;
	private String caracter;
	private String curso;
	
	private ArrayList<Grupo> grupos = new ArrayList();
	
	public Asignatura(String id, String nombre, int creditos, String caracter, String curso) {
		this.id=id;
		this.nombre=nombre;
		this.creditos=creditos;
		this.caracter=caracter;
		this.curso=curso;
	}

	public void anyadirGrupo(Grupo grupo) {
		this.grupos.add(grupo);
	}
	
}