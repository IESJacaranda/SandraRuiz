package relacion7.ej5;

import java.util.Objects;

import relacion7.ej2.Producto;

public class Equipo {
	
	private String nombre;
	private String ciudad;
	private int anyo;
	private String presidente;
	private String estadio;
	
	public Equipo () {}
	
	public Equipo (String nombre, String ciudad, int anyo, String presidente, String estadio) {
		this.nombre=nombre;
		this.ciudad=ciudad;
		this.anyo=anyo;
		this.presidente=presidente;
		this.estadio=estadio;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCiudad() {
		return ciudad;
	}

	public void setCiudad(String ciudad) {
		this.ciudad = ciudad;
	}

	public int getAnyo() {
		return anyo;
	}

	public void setAnyo(int anyo) {
		this.anyo = anyo;
	}

	public String getPresidente() {
		return presidente;
	}

	public void setPresidente(String presidente) {
		this.presidente = presidente;
	}

	public String getEstadio() {
		return estadio;
	}

	public void setEstadio(String estadio) {
		this.estadio = estadio;
	}

	@Override
	public int hashCode() {
		return Objects.hash(nombre);
	}

	@Override
	public boolean equals(Object obj) {
		boolean sonIguales = false;
		if(this==obj) {
			sonIguales = true;
		}else if (obj!=null 
				&& obj instanceof Equipo
				&& ((Equipo)obj).hashCode()==this.hashCode()) {
			sonIguales = true;
		}
		return sonIguales;
	}	
	
}
