package exemplos;

public class Exemplo01 {

	public static void main(String[] args) {
		// Conheço os valores do array (listas com tamanho determinado) previamente.
		
		int[] numeros = {2,4,6,8,10};
		
		System.out.println("Tamanho: " + numeros.length);
		
		System.out.println("Primeiro: " + numeros[0]);
		System.out.println("Último: " + numeros[4]);
		
		for (int i = 0; i < numeros.length; i++) {
			System.out.print(numeros[i] + " ");
		}
		
		System.out.println();
		
		// Imprimir os números do array usando while.
		
		int i = 0;
		while (i < numeros.length) {
			System.out.print(numeros[i] + " ");
			i++;
		}
		
		System.out.println();
		
		for (int j = numeros.length - 1; j >= 0; j--) {
			System.out.print(numeros[j] + " ");
		}
		
	}

}
