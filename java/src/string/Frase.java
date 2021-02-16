package string;

public class Frase {
	
	private String frase;
	
	public Frase(String frase) {
		this.frase = frase;
		
	}
	
	public int contarPalabras() {
		int numeroPalabras = 0;
		
		this.frase = this.frase.trim();
		while(this.frase!=this.frase.replace("  ", " ")) {
			this.frase = this.frase.replace("  ", " ");
		}
			
		for(int i = 0; i < this.frase.length(); i++) {
			if(this.frase.charAt(i)==' ') {
				numeroPalabras++;
			}
		}
		
		return numeroPalabras+1;
				
	}
}
