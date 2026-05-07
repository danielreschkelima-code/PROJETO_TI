package exemplos;

import java.util.Scanner;

public class Exemplo03 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe o tamanho do array: ");
		int t = Integer.parseInt(leitor.nextLine());
		System.out.println("\nInforme os números das posições...\n");
		
		int[] numeros = new int[t];
		
		for (int i = 0; i < numeros.length; i++) {
			System.out.print("Posição " + i + ": ");
			int posiçãoi = Integer.parseInt(leitor.nextLine());
			numeros[i] = posiçãoi;				
		}
		
		System.out.println();
		System.out.println("LISTA DO USUÁRIO:");
		
		int soma = 0;
		for (int i = 0; i < numeros.length; i++) {
			System.out.println("Posição " + i + ": " + numeros[i]);
			soma += numeros[i];
		}
		
		// Imprimir a soma dos números do array.
		
		System.out.println("\n A SOMA DOS NÚMEROS DO ARRAY É: " + soma + ".");
		
	}

}
