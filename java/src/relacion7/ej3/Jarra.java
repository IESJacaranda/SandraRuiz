package relacion7.ej3;

public class Jarra {

	private double capacidad;
	private double cantidadAgua;
	private double totalAguaConsumida;
	
	public Jarra() {}
	
	public Jarra(double capacidad) {
		this.capacidad = capacidad;
		this.cantidadAgua = 0.0;
	}

	public void llenarJarra() throws Exception {
		if(this.cantidadAgua<this.capacidad
				|| this.capacidad==0) {
			this.cantidadAgua = this.capacidad;
			System.out.println("La jarra se ha llenado correctamente");
		}else {
			throw new Exception("La jarra no se puede llenar");
		}
	}
	
	public void vaciarJarra() throws Exception {
		if(this.cantidadAgua==this.capacidad || this.capacidad>0) {
			this.totalAguaConsumida=this.cantidadAgua;
			this.cantidadAgua = 0.0;
			System.out.println("La jarra se ha vaciado correctamente");
		}else {
			throw new Exception("La jarra no se puede vaciar");
		}
		
	}
	
	public void volcarJarra(Jarra jarra) throws Exception {
		if(jarra.getCantidadAgua()<jarra.getCapacidad() && this.cantidadAgua!=0) {			
			while(jarra.getCantidadAgua()<jarra.getCapacidad() && this.cantidadAgua>0) {
				this.cantidadAgua-=1;
				jarra.setCantidadAgua(jarra.getCantidadAgua()+1);
			}
			System.out.println("La jarra se ha volcado correctamente.");
		}else{
			throw new Exception("No se puede volcar la cantidad de la jarra.");
		}
			
	}
	
	
	public double getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(double capacidad) {
		this.capacidad = capacidad;
	}

	public double getCantidadAgua() {
		return cantidadAgua;
	}

	public void setCantidadAgua(double cantidadAgua) {
		this.cantidadAgua = cantidadAgua;
	}

	public double getTotalAguaConsumida() {
		return totalAguaConsumida;
	}

	public void setTotalAguaConsumida(double totalAguaConsumida) {
		this.totalAguaConsumida = totalAguaConsumida;
	}


	@Override
	public String toString() {
		return "Su capacidad es de: "+ this.capacidad +" litros"
				+ " y ahora contiene: " + this.cantidadAgua +" litros.";
	}
	
}
