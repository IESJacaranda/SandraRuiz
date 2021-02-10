package poo4;

public class Complejo {

	private double real;
	private double imaginaria;
	
	
	public Complejo() {}
	
	
	public Complejo(double real, double imaginaria) {
		this.real = real;
		this.imaginaria = imaginaria;
		
	}
	
	public static Complejo suma(double realC1, double imC1, double realC2, double imC2) {
		double sumaReal = realC1+realC2;
		double sumaIm = imC1+imC2;
		
		Complejo resultadoSuma = new Complejo(sumaReal, sumaIm);
		return resultadoSuma;
	}

	
	public Complejo suma(Complejo complejoASumar) {
		return new Complejo(this.getReal() + complejoASumar.getReal(),
				this.getImaginaria() + complejoASumar.getImaginaria());
		
	}
	
	public static Complejo resta(double realC1, double imC1, double realC2, double imC2) {
		double restaReal = realC1-realC2;
		double restaIm = imC1-imC2;
		
		Complejo resultadoResta = new Complejo(restaReal, restaIm);
		return resultadoResta;
	}
	/**
	 * Este método resta el valor de dos números complejos (this y recibido
	 * como argumento y lo devuelve en un nuevo objeto
	 * @param complejoARestar variable compleja a restar
	 * @return número complejo con el resultado de la resta
	 */
	public Complejo resta(Complejo complejoARestar) {
		return new Complejo(this.getReal() - complejoARestar.getReal(),
				this.getImaginaria() - complejoARestar.getImaginaria());
		
	}
	
	
	@Override
	public String toString() {
	
		return (this.real + " + "+ this.imaginaria + "i");
	}
	
	
	@Override
	public boolean equals(Object obj) {
		boolean sonIguales = false;
		
		if(this==obj) {
			sonIguales = true;
		
		}else if (obj instanceof Complejo) {
			if(((Complejo) obj).getImaginaria()==this.getImaginaria()
				&& ((Complejo) obj).getReal()==this.getReal()
				)
				{
				sonIguales=false;
				}
		}
		return sonIguales;		
	}
	
	
	public double getReal() {
		return real;
	}

	
	public void setReal(double real) {
		this.real = real;
	}

	public double getImaginaria() {
		return imaginaria;
	}

	public void setImaginaria(double imaginaria) {
		this.imaginaria = imaginaria;
	}


	public String equalsComplejo(Complejo b) {
		// TODO Auto-generated method stub
		return null;
	}
}