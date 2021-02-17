package examen.febrero.ej1;

public class Contestador {
	
	private String mensaje1;
	private String mensaje2;
	private String mensaje3;
	
	public final String CADENA_VACIA = "";
	
	
	
	public Contestador() {
		borrarTodosLosMensajes();
	}

	
	public boolean isBuzonLleno() {
		return (mensaje1!=CADENA_VACIA 
				&& mensaje2!=CADENA_VACIA 
				&& mensaje3!=CADENA_VACIA);
	}
	
	public int getNumeroMensajes() {
		int numero = 0;
		if(mensaje1!=null && mensaje1!=CADENA_VACIA) {
			numero++;
		}
		if(mensaje2!=null && mensaje2!=CADENA_VACIA) {
			numero++;
		}
		if(mensaje3!=null && mensaje3!=CADENA_VACIA) {
			numero++;
		}
		return numero;
	}
	
	public void addMensaje(String mensaje) throws Exception {
		if(isBuzonLleno()) {
			throw new Exception("El buzón está lleno, prueba mejor en otro momento");
		}else if (mensaje==null || mensaje.isEmpty()) {
			throw new Exception("Debe indicar un mensaje");
		}else {
			if(this.mensaje1==null && this.mensaje1==CADENA_VACIA) {
				setMensaje1(mensaje);
			}else if(this.mensaje2==null && this.mensaje2==CADENA_VACIA) {
				setMensaje2(mensaje);
			}else if(this.mensaje3==null && this.mensaje3==CADENA_VACIA) {
				setMensaje3(mensaje);
			}
		}
	}
	



	public void borrarTodosLosMensajes() {
		borrarMensaje1();
		borrarMensaje2();
		borrarMensaje3();
	}
	
	public void borrarMensaje1() {
		setMensaje1(CADENA_VACIA);
	}
	
	public void borrarMensaje2() {
		setMensaje2(CADENA_VACIA);	
	}
	
	public void borrarMensaje3() {
		setMensaje3(CADENA_VACIA);
	}
	
	
	
	
	
	
	
	public String getMensaje1() throws Exception {
		if(mensaje1==null || mensaje1.isBlank()) {
			throw new Exception("El mensaje solicitado no existe");
		}
		return mensaje1;
	}

	public void setMensaje1(String mensaje1) {
		this.mensaje1 = mensaje1;
	}

	public String getMensaje2() throws Exception {
		if(mensaje2==null || mensaje1.isBlank()) {
			throw new Exception("El mensaje solicitado no existe");
		}
		return mensaje2;
	}

	public void setMensaje2(String mensaje2) {
		this.mensaje2 = mensaje2;
	}

	public String getMensaje3() throws Exception {
		if(mensaje3==null || mensaje1.isBlank()) {
			throw new Exception("El mensaje solicitado no existe");
		}
		return mensaje3;
	}

	public void setMensaje3(String mensaje3) {
		this.mensaje3 = mensaje3;
	}
	
	
	
	
	
	
	
	
}
