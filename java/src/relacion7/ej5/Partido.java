package relacion7.ej5;

import java.util.Objects;

public class Partido {
	
	private int golesLocal;
	private int golesVisitante;
	private int jornada;
	private Equipo local;
	private Equipo visitante;
	private char quiniela;

	
	
	public Partido() {}
	
	public Partido(int golesLocal, int golesVisitante, int jornada) {
		this.golesLocal = golesLocal;
		this.golesVisitante = golesVisitante;
		this.jornada = jornada;
	}

	
	public int getGolesLocal() {
		return golesLocal;
	}


	public int getGolesVisitante() {
		return golesVisitante;
	}

	
	public int getJornada() {
		return jornada;
	}

	public void setJornada(int jornada){
		if(jornada>=1 && jornada<=38) {
			this.jornada = jornada;
		}
		
	}


}
