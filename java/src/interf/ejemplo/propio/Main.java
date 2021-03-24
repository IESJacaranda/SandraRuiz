package interf.ejemplo.propio;

public class Main {

	public static void main(String[] args) {
		
		
		Quiroptero murcielago = new Murcielago(20, 2, 3, "Fruta");
		Murcielago murci = (Murcielago) murcielago;
		System.out.println(murci.seAlimenta());
		System.out.println(murcielago.getNumeroMamas());
		System.out.println(murcielago.getTiempoGestacion());
		
		Delfin delfin = new Delfin (30, 2, 11, "Peces", 50);
		System.out.println(delfin.tieneBranquias());
		System.out.println(delfin.getNumeroMamas());
		System.out.println(delfin.getTiempoGestacion());
		System.out.println(delfin.tipoAlimentacion());
		
		Pinguino pinguino = new Pinguino(20, "Animales marinos", 2);
		System.out.println(pinguino.getPeso());
		System.out.println(pinguino.tieneBranquias());
		System.out.println(pinguino.tipoAlimentacion());
		
	}

}
