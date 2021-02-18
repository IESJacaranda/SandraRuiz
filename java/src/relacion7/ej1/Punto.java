package relacion7.ej1;

public class Punto {

	private double x;
	private double y;
	
	
	public Punto(double x, double y) {
		this.x = x;
		this.y = y;
			
	}


	public double getX() {
		return x;
	}


	public void setX(double x) {
		this.x = x;
	}


	public double getY() {
		return y;
	}


	public void setY(double y) {
		this.y = y;
	}


	@Override
	public boolean equals(Object obj) {
		boolean result = false;
		
		if(this==obj) {
			result = true;
		}else if(obj!=null && obj instanceof Punto) {
			if(((Punto)obj).getX()==this.getX() && ((Punto)obj).getY()==this.getY()) {
				result = true;
			}
				
		}
		return result;
	}
	
	
	
}

