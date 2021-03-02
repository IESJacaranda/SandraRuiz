package galaxia;

public class Main {

	public static void main(String[] args) {
	

		Pelicula peli = new Pelicula();
		Personaje p1 = new Personaje("Yoda", 80, peli, 58, "Yoda", 30);
		Personaje p2 = new Personaje("Luke Skywalker", 67, peli, 180, "Humano", 80);
		Personaje p3 = new Personaje("Darth Vader", 100, peli, 190, "Humano", 70);

		
		System.out.println(p1.toString());
		System.out.println(p2.toString());
		System.out.println(p3.toString());
		
		Pelicula peli1 = new Pelicula("Star Wars: Episodio III. La venganza de los Sith", 2005, p1, p2, p3);
		Pelicula peli2 = new Pelicula("Star Wars: Episodio I. La amenaza fantasma", 1999, p1, p2, p3);
		
		System.out.println(peli1.compararPelicula(peli2));
		
		System.out.println(peli1.obtenerMaximoPoderPelicula());
		
		System.out.println(peli1.obtenerPoderPelicula());
		
		System.out.println(peli1.toString());
	}
}
