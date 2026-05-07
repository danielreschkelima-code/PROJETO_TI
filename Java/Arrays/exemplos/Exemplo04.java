package exemplos;

import java.util.Scanner;

public class Exemplo04 {

	public static void main(String[] args) {

		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe o tamanho do array: ");
		int t = Integer.parseInt(leitor.nextLine());
		
		double[] valores = new double[t];
		
		System.out.println();
		for (int i = 0; i < valores.length; i++) {
			System.out.println("Informe o " + (i+1) + "º valor: ");
			valores[i] = Double.parseDouble(leitor.nextLine());
		}
		
		// Imprimir a média dos valores do array.
		
		float soma = 0;
		for (int i = 0; i < valores.length; i++) {
			soma += valores[i];
		}
		
		float média = soma/valores.length;
		System.out.println("\nMédia aritmética do array: " + média + ".");
	}

}
