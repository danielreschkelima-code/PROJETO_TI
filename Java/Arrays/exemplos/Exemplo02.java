package exemplos;

public class Exemplo02 {

	public static void main(String[] args) {
		// EU não conheço previamente os valores a serem guardados no array.
		
		int[] numeros = new int[5];
				
		numeros[0] = 123;
		numeros[2] = 456;
		numeros[4] = 789;
		
		for (int i = 0; i < numeros.length; i++) {
			System.out.print(numeros[i] + " ");
		}

	}

}
