package relacion7.ej5;

import java.util.Objects;

public class Partido {
	
	private int golesLocal = 0;
	private int golesVisitante = 0;
	private int jornada;

	
	
	public Partido() {}
	
	public Partido(int golesLocal, int golesVisitante, int jornada) {
		this.golesLocal = golesLocal;
		this.golesVisitante = golesVisitante;
		this.jornada = jornada;
	}

	
	public int getGolesLocal() {
		return golesLocal;
	}

	public void setGolesLocal(int golesLocal) {
		this.golesLocal = golesLocal;
	}

	public int getGolesVisitante() {
		return golesVisitante;
	}

	public void setGolesVisitante(int golesVisitante) {
		this.golesVisitante = golesVisitante;
	}

	public int getJornada() {
		return jornada;
	}

	public void setJornada(int jornada) {
		this.jornada = jornada;
	}


}
