package relacion7.ej2;

import java.util.Objects;

public class Producto {
	
	private int codigo;
	private String descripcion;
	private double precio;
	
	private static double iva = 20.0; // es una propiedad compartida por todos los productos, por lo que si se cambia a uno, se cambia a todos.
	
	
	public Producto() {}
	
	
	public Producto(String descripcion, double precio) {
		this.descripcion = descripcion;
		this.precio = precio;
	}


	public int getCodigo() {
		return codigo;
	}


	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}


	public String getDescripcion() {
		return descripcion;
	}


	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}


	public double getPrecio() {
		return precio;
	}


	public void setPrecio(double precio) {
		this.precio = precio;
	}


	public double getIva() {
		return iva;
	}


	public void setIva(double iva) {
		this.iva = iva;
	}


	@Override
	public int hashCode() {
		return Objects.hash(descripcion, precio);
		
		//return this.descripcion.hashCode()
		//+ String.valueOf(this.precio).hashCode();
	}


	@Override
	public boolean equals(Object obj) {
		boolean sonIguales = false;
		if(this==obj) {
			sonIguales = true;
		}else if (obj!=null 
				&& obj instanceof Producto
				&& ((Producto)obj).hashCode()==this.hashCode()) {
			sonIguales = true;
		}
		return sonIguales;
	}


	@Override
	public String toString() {
		return "{descripción: " + this.descripcion +
				", precio: " + this.precio +
				", iva: " + this.iva +
				", código: " + this.hashCode() +
				", precio: " + this.calcularPrecioConIva() 
				+ "}";
	}

	
	public double calcularPrecioConIva() {
		return this.precio*(1+this.iva/100);
	}
	
	
	public String getPrecioConIva() {
		return "El precio total del producto es: " + this.calcularPrecioConIva();
	}
	
}
