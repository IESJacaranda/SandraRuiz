package uml.java_3h;

import java.util.ArrayList;

public class Profesor {
	private String nrp;
	private String nombre;
	private String categoria;
	private String area;
	
	public Departamento departamento;
	public Departamento dirige;
	
	private ArrayList<Grupo> grupos = new ArrayList();
	
	public Profesor(String nrp, String nombre, String categoria, String area) {
		this.nrp=nrp;
		this.nombre=nombre;
		this.categoria=categoria;
		this.area=area;
	}
	
	
	public void dirige(Departamento dpto) {
		this.dirige=dpto;
	}
	
	public void asignarGrupos(Grupo grupo) {
		this.grupos.add(grupo);
	}
}
