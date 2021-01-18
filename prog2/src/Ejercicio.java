package method;



public class Ejercicio {
	
	public static final Double PI = 3.14;
	

	public static void main(String[] args) {
				
		// Variables
		
		// Inicio	
				
	}
	
	public static int numeroSolucionesEcuacionSegundoGrado(int a, int b, int c) { 
		//este metodo devuelve el numero de soluciones de una ec2ºgrado
		//ax2 + b + c = 0
		// el primer int significa que devolvera int
		//Si es negativo, no tiene solucion. 
		//Si es 0, tendra 1 solucion. 
		//Si es mayor que 0, tendra 2 soluciones.
		
		
		int radical;
		radical = b*b - 4*a*c;
		int solucion;
		solucion = 0;
		
		if (a==0) {
			solucion = -1;
		}
		else if (radical<0) {
			solucion = 0;
		}
		else if (radical==0) {
			solucion = 1;
		}
		else if (radical>0) {
			solucion = 2;
		}
		return solucion;
		
	}
	
	
	public static Double solucionSumaEcuacionSegundoGrado(int a, int b, int c) {
		//este metodo devuelve la suma de una ecuacion de 2grado
		 //x=(-b+raiz(b^2-4ac)/2a
		//devuelva -1000 si no tiene solucion
		//devuelva una solucion si solo tiene una
		//dos soluciones si tiene dos
		
		int numSol = numeroSolucionesEcuacionSegundoGrado(a,b,c);
		
		if (numSol == 0 || numSol == -1) {
			return -1000.0;
		}
		else if (numSol == 1) {
			return (double) -b/(2*a);
		}
		else {
			Double aux = ((double)-b+Math.sqrt(b*b-4*a*c))/(2*a);
			return aux;
		}
			
	}
	
	
	public static Double solucionRestaEcuacionSegundoGrado(int a, int b, int c) {
		//este metodo devuelve la resta de una ecuacion de 2grado
		 //x=(-b+raiz(b^2-4ac)/2a
		//devuelva -1000 si no tiene solucion
		//devuelva una solucion si solo tiene una
		//dos soluciones si tiene dos
		
		int numSol = numeroSolucionesEcuacionSegundoGrado(a,b,c);
		
		if (numSol == 0 || numSol == -1) {
			return -1000.0;
		}
		else if (numSol == 1) {
			return (double) -b/(2*a);
		}
		else {
			Double aux = ((double)-b-Math.sqrt(b*b-4*a*c))/(2*a);
			return aux;
		}
		
	}	
	
	
	public static Double areaCirculo(Double r) {
		//este metodo calcula el area de un circulo
		//A=pi*r^2
		
		double area;
		
		area = PI*r*r;
				
		return area;
		
	}
	
	
	public static Double longitudCirculo(Double r) {
		//este metodo calcula la longitud de un circulo
		//longitud = 2*PI*r
		
		double longitud;
		
		longitud = 2*PI*r;
		
		return longitud;
		
	}
	
	
	public static boolean esMultiplo(int a, int b) {
		//este metodo devuelve true si a es multiplo de b
		
		boolean solucion = true;
		
		if (a==0 || b==0) {
			solucion = false;
		}
		else if (a%b==0){
			solucion = true;
		}
		else {
			solucion = false;
		}
		return solucion;
		
	}
	
	
	public static int horaMayor(int hora1, int min1, int seg1, int hora2, int min2, int seg2) {
		//este metodo devuelve cual hora es mayor de dos horas dadas
		int segundos1;
		int segundos2;
		int resultado;
		resultado = 0;
		
		segundos1 = hora1*3600 + min1*60 + seg1;
		segundos2 = hora2*3600 + min2*60 + seg2;
		
		if (hora1 >12 || hora1<0 || hora2 >12 || hora2<0){
			resultado = -1000;
		}
		else if (min1 >59 || hora1<0 || min2 >59 || min2<0){
			resultado = -1000;
		}
		else if (seg1 >59 || seg1<0 || seg2 >59 || seg2<0){
			resultado = -1000;
		}
		else if (segundos1>segundos2) {
			resultado = 1;
		}
		else if (segundos1<segundos2) {
			resultado = 2;
		}
		else if (segundos1==segundos2) {
			resultado = 0;
		}
		
		return resultado;
		
		
	}
	
	
	public static int segundosEntre(int hora1, int min1, int seg1, int hora2, int min2, int seg2) {
		
		int resultado;
		resultado = 0; 
		
		if (hora1 >12 || hora1<0 || hora2 >12 || hora2<0){
			resultado = -1000;
		}
		else if (min1 >59 || hora1<0 || min2 >59 || min2<0){
			resultado = -1000;
		}
		else if (seg1 >59 || seg1<0 || seg2 >59 || seg2<0){
			resultado = -1000;
		}
		else if (seg1<seg2) {
			resultado = -1000;
		}
		else if (seg1>seg2) {
			resultado = seg1-seg2;
		}
		return resultado;
	}
	
	
	public static int maximoComunDivisor(int a, int b) {
		//este metodo devuelve el maximo comun divisor de dos numeros
		//se resta el menor al mayor hasta que ambos sean iguales
		//el numero menor que se obtenga sera el mcd
		
		while (a != b) {
			if (a>b) {
				a = a-b;
			}
			else {
				b = b-a;
			}
		}
		return a;
	}
	
	public static int minimoComunMultiplo(int a, int b) {
		//este metodo devuelve el minimo comun multiplo de dos numeros
		//El mcm de dos números = al producto de los números dividido entre su mcd. 
		
		int mcd = maximoComunDivisor(a,b);
		int mcm;
		mcm = (a*b)/mcd;
		
		return mcm;
	}
	
	public static String binario(int num) {
		
	}
	
	public static int decimal(String num) {
		
	}
}
