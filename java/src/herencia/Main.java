package herencia;

public class Main {
	
	public static void main(String[] args) {
		
	Bebe bebe1 = new Bebe();
	bebe1.desplazarse();
	bebe1.obtenerHabitos();
	
	System.out.println("---------------");
	Adulto adulto1 = new Adulto();
	adulto1.desplazarse();
	adulto1.obtenerHabitos();
	
	System.out.println("---------------");
	Anciano anciano1 = new Anciano();
	anciano1.conducir();
	anciano1.desplazarse();
	anciano1.obtenerHabitos();
	
	System.out.println("---------------");
	//POLIMORFISMO
	
	Persona persona = new Bebe();
	persona.desplazarse(); //usa lo de Bebe
	persona.obtenerHabitos(); //usa lo de Bebe
	//((Adulto)persona).conducir(); //EL BEBÉ NO PUEDE CONVERTIRSE EN ADULTO, PQ PARA CONVERTIR UNA JERARQUÍA EN OTRA TIENE QUE ESTAR EN LA MISMA RAMA DE LA JERARQUÍA
	
	System.out.println("---------------");
	persona = new Adulto();
	persona.desplazarse(); //ahora usa lo de Adulto
	persona.obtenerHabitos(); //ahora usa lo de Adulto
	((Adulto)persona).conducir(); //hacemos el casting para cambiar la asignación de la variable y que sea Adulto
	
	System.out.println("---------------");
	persona = new Anciano();
	persona.desplazarse();
	persona.obtenerHabitos(); 
	((Adulto)persona).conducir(); //en este caso sí se puede hacer el casting porque Anciano extiende de Adulto, están en la misma rama de la jerarquía
	
	
	/*Dentro de la interfaz Collection vamos a usar:
	 * - Las List, con los ArrayList
	 * - Las Sef, con HashSef
	 */
	}
}
