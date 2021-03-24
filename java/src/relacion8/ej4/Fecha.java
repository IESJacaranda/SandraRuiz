package relacion8.ej4;

public class Fecha {
	
	private int day;
	private int month;
	private int year;
	
	private final static String[] MONTHS = {"Enero", "Febrero", "Marzo", "Abril", "Mayo",
								"Junio","Julio","Agosto","Septiembre","Octubre",
								"Noviembre", "Diciembre"};
	
	private final static int[] DAYS_IN_A_MONTH = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	public Fecha() {
		super();
	}

	public Fecha(int day, int month, int year) throws FechaNoValidaException {
		this(); //llama al constructor vacío
		if(esFechaValida(day, month, year)) {
			this.day = day;
			this.month = month;
			this.year = year;
		}else {
			throw new FechaNoValidaException();
		}
		
	}
	
	
	private boolean esFechaValida(int day, int month, int year) {
		boolean result = false;
		if(day> 0 && month >0) {
			if(DAYS_IN_A_MONTH[month-1]>=day) {
				result =  true;
			}else if(isLeapYear(year) && month==2 && day==29) { //solo comparo para 29, pq el 28 ya lo tengo recogido en el if
				result = true;
			}
			
		}return result;
	}
	
	private boolean isLeapYear(int year) {
		return year%4==0 && year%100!=0 || year%400==0;
	}
	
	
	
	//Operador ternario, conocido en algunas implementaciones como operador Elvis ?:
	
	//(condicion)  
	//? devuelvo en condicion true
	//: devuelvo en condicion false
	public String pasarAFormatoLargo() {
		return (month>0)? "La fecha en formato largo es "+this.day + " de" + MONTHS[this.month-1] 
				+ " de "+ this.year
				: "";
		
	}
		
}
