package relacion7.ej2;

public class Principal {

	
	
	
	public static void main(String[] args) {
		
		Producto tv = new Producto("Televisión", 500.0);
		Producto radio = new Producto("Radio", 20.0);
		Producto ordenador = new Producto("Ordenador", 2000.0);
		
		Producto tv2 = new Producto("Televisión", 500.0);
		
		Producto tv3 = new Producto("Televisión Samsung", 500.0);
		
		tv.setIva(21); //cambia el iva de todos los productos
		//tv.setIva(19.5); //vuelve a cambiar el iva y se queda con este último
		
		System.out.println(tv);
		System.out.println(radio);
		System.out.println(ordenador);
		
		/*
		System.out.println(tv.hashCode());
		System.out.println(tv2.hashCode());
		System.out.println(radio.hashCode());
		System.out.println(ordenador.hashCode());
		
		System.out.println(tv.equals(tv2));
		System.out.println(tv.equals(tv3));
		
		System.out.println(tv2.getPrecioConIva());
		*/
	}

}
