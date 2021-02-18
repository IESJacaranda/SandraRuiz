package relacion7.ej1;

public class Main {

	public static void main(String[] args) {
		
		Punto puntito1 = new Punto(5.0, 3.0);
		Punto puntito2 = new Punto(4.0, 2.0);
		Punto puntito3 = new Punto(5.0, 3.0);
		Punto puntito4 = new Punto(4.0, 2.0);
		
		//System.out.println(puntito1.equals(puntito2));

		Linea linea1 = new Linea(puntito1,puntito2);
		Linea linea2 = new Linea(puntito3,puntito4);
		
		System.out.println(linea1.equals(linea2));
		
	}

}
