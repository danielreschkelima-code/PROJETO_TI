package exemplos;

import java.util.Scanner;

public class Exemplo05 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe uma palavra: ");
		String palavra = leitor.nextLine();
		
		System.out.println("Tamanho: " + palavra.length());
		System.out.println("Char específico: " + palavra.charAt(0)); // posição do array string.
		
		for (int i = 0; i < palavra.length(); i++) {
			System.out.println(palavra.charAt(i));
		}

	}

}
