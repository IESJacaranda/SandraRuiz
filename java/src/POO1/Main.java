package POO1;

/*import java.util.Scanner;*/

public class Main {

	
	public static void main(String[] args) {
		
		Rectangulo rectangulo = new Rectangulo();
		
		
		rectangulo = new Rectangulo(3, 5);
		/*Scanner teclado;
		
		System.out.println("Introduzca la longitud");
		teclado = new Scanner(System.in);
		rectangulo.setLongitud(Double.parseDouble(teclado.nextLine()));
		
		System.out.println("Introduzca el ancho");
		rectangulo.setAncho(Double.valueOf(teclado.nextLine()));*/
		
		System.out.println(rectangulo.getArea());
		System.out.println(rectangulo.getPerimetro());
		System.out.println(rectangulo);
	}
}
