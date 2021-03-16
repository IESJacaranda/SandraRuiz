package matrices.ejemplo;


public class Matriz {
	
	
	public static final String CORCHETE_APERTURA = "[";
	public static final String CORCHETE_CIERRE = "]";
	public static final String SEPARADOR = ",";
	public static final String SALTO_LINEA = "\n";
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		/*trabajandoConMatrix();
		
		int[][] matrix = {{1,2,3}, {4,5}, {6,7,8,9}};
		System.out.println(formateaAString(matrix));
		
		int[][] matrizA = {{1,2}, {3,4}};
		int[][] matrizB = {{1,2}, {3,4}};
		System.out.println(formateaAString(sumarMatrices(matrizA, matrizB)));
	*/
		int[] vector1 = {3,2};
		int[] vector2 = {5,15,23};
		System.out.println(formateaAString(concatenarVectores(vector1,vector2)));
		
		int[][] matriz1= {{3,1,0},{0,2,4},{0,5,1}};
		int[][] matriz2= {{0,0,3},{5,2,1},{1,4,0}};
		int[][] matriz3= {{0,4,1},{1,2,5},{3,0,0}};
		int[][] matriz4= {{0,4,1},{1,7,5},{3,0,0}};
		System.out.println(formateaAString(matriz2));
		System.out.println(formateaAString(rotarMatriz(matriz1)));
		System.out.println(formateaAString(rotarMatriz(rotarMatriz(matriz1))));
		System.out.println(formateaAString(rotarMatriz(rotarMatriz(rotarMatriz(matriz1)))));
		try {
			System.out.println(sonMatricesIguales(rotarMatriz(matriz1),matriz2));
		} catch (Exception e) {
			System.out.println(e.getMessage());
		}

	    int[][] matriz5= {{3,1,0,1},{0,2,4}};
	    System.out.println(formateaAString(matriz5));
	    System.out.println(formateaAString(rotarMatrizNoCuadrada(matriz5)));
	}

	/** Ejercicio 1
	 * Este método genera una matriz cuadrada con 1 en diagonal.
	 */
	public static void trabajandoConMatrix() {
		
		/*int[] vector = new int[3];
		System.out.println(vector);
		
		System.out.println(vector[vector.length-2]);
		*/
		
		
		/*int[][] matrix;
		matrix = new int[3][2];
	
		for(int i=0; i<matrix.length; i++) {
			for(int j=0; j<matrix[i].length; j++) {
				matrix[i][j]=1;
				System.out.println(matrix[i][j]);
			}
		}*/
		
		/*int[][] matrix = new int [4][4];
		
		for (int i=0; i<matrix.length;i++) { //recorre las filas
			matrix[i][i] = 1;
			for(int j=0;j<matrix[i].length;j++) { //recorre las columnas
				System.out.print(matrix[i][j] + " ");	
			}System.out.println();
		}
		System.out.println("---------");
	
		int [][] matrix2 = {{5,5,5,5},{5,5,5,5}, {5,5,5,5}, {5,5,5,5}};
		for (int i=0; i<matrix2.length;i++) { //recorre las filas
			matrix2[i][i] = 1;
			for(int j=0;j<matrix2[i].length;j++) { //recorre las columnas
				System.out.print(matrix2[i][j] + " ");	
			}System.out.println();
		}
	*/	
		
	}
	
	/** Ejercicio 2
	 * Este método recibe una matriz y convierte su formato añadiéndole
	 * corchetes de inicio, de cierre y separando los elementos por comas.
	 * @param matriz cuadrada
	 * @return matriz formateada
	 */
	public static String formateaAString(int[][] matriz) {
		
		StringBuilder sb = new StringBuilder();
		
		if(matriz!=null && matriz.length>0) {
			for (int i=0; i<matriz.length;i++) { //recorre las filasÇ
				for(int j=0;j<matriz[i].length;j++) { //recorre las columnas	
					if(j==0) {
						sb.append(CORCHETE_APERTURA);
					}
					sb.append(matriz[i][j]);
										
					if(j==matriz[i].length-1) {
						sb.append(CORCHETE_CIERRE);
						
					}else {
						sb.append(SEPARADOR);
					}
				}
				sb.append(SALTO_LINEA);
			}
		
				
		}
		
		return sb.toString();
	
	}
	/**Ejercicio 4, parte 1
	 * Este método recibe un vector y llama al metodo formateaAString 
	 * @param vector
	 * @return vector convertido en matriz
	 */
	public static String formateaAString(int[] vector) {
		
		return formateaAString(new int [][] {vector});
	}
	
	/** Ejercicio 3
	 * Este metodo suma dos matrices de igual dimension (columnas y filas)
	 * y devuelve una matriz con el resultado
	 * @param matrizA matriz izquierda
	 * @param matrizB matriz derecha
	 * @return matriz resultado
	 */
	public static int[][] sumarMatrices(int[][]matrizA, int[][] matrizB) {
		
		int[][] resultado = null;
		
		if(matrizA!=null && matrizB!=null
			&& matrizA.length==matrizB.length
			&& matrizA[0].length==matrizB[0].length) {
			
			resultado= new int[matrizA.length][matrizA[0].length];
			
			for(int i=0;i<matrizA.length;i++) {
				for(int j=0;j<matrizA[i].length;j++) {
					resultado[i][j] = matrizA[i][j] + matrizB[i][j];
			
				}
			}
		}
		return resultado;
	}
	
	/** Ejercicio 4, parte 2
	 * Este método recibe dos vectores y los concatena
	 */
	
	public static int[] concatenarVectores(int[] v1, int[] v2) {
		
		int [] resultado = null;
		
		if(v1!=null && v2!=null) {
			resultado = new int[v1.length+v2.length];
			for(int i=0; i<v1.length;i++) {
				resultado[i]=v1[i];
			}
			for(int i=0; i<v2.length;i++) {
				resultado[i+v1.length]=v2[i];
			}
		
		}
		return resultado;
		
	}

	
	/**Ejercicio 5, parte 1
	 * Este método recibe una matriz cuadrada y la rota a la derecha
	 * @param matriz
	 * @return matriz rotada a la derecha
	 */
	
	public static int[][] rotarMatriz(int[][] matriz) {
		int size = matriz.length;

	    int[][] newMatriz = new int[size][size];

	    for(int i=0; i<size; i++) {
	        for(int j=0; j<size; j++) {
	            newMatriz[j][size-1-i] = matriz[i][j];
	        }               
	    }
	    return newMatriz;
	}    
	    
	/**Ejercicio 5, parte 2
	 * Este método recibe dos matrices y las compara, comprobando si son
	 * la misma pero rotada.
	 * @param matrix1
	 * @param matrix2
	 * @return true si son la misma matriz, false si no lo son.
	 */

    public static boolean sonMatricesIguales(int[][]matrix1, int[][]matrix2) throws Exception {
    	boolean sonIguales = true;
    	
    	if(matrix1!=null && matrix2!=null && matrix1.length==matrix2.length 
    			&& matrix1[0]!=null && matrix2[0]!=null 
    			&& matrix1[0].length== matrix2[0].length) {
    		for(int i=0; i<matrix1.length && sonIguales;i++) {
    			for(int j=0; j<matrix1[i].length && sonIguales;j++) {
    				if(matrix1[i][j] != matrix2[i][j]) {
    					sonIguales = false;
    				}
    			}
    		}
    	}else {
    		throw new Exception ("Las matrices no se pueden comparar");
    	}
    	
    	
    	return sonIguales;
    }
    
    
    /**Ejercicio 6
     * No funciona.
     * @param matriz
     * @return
     */
    	
    public static int[][] rotarMatrizNoCuadrada(int[][] matriz) {

	    int fila=0;
	    int columna=0;
	    
		int[][] newMatriz = new int[fila][columna];
		int k;
		
	    for(int i=0; i<fila; i++) {
	    	k=0;
	        for(int j=fila-1; j>=0; j--) {
	            newMatriz[i][k] = matriz[j][i]; 
	            k++;
	        }               
	    }
	    return newMatriz;
	}    
}


