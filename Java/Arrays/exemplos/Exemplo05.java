package exemplos;

import java.util.Scanner;

public class Exemplo05 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe o tamanho do array: ");
		int t = Integer.parseInt(leitor.nextLine());
		
		//String NÃO é um dado primitivo, é uma classe.
		
		String[] nomes = new String[t];
		
		for (int i = 0; i < nomes.length; i++) {
			System.out.print("Informe o " + (i+1) + " º nome: ");
			nomes[i] = leitor.nextLine();
		}
		
		for (int j = 0; j < nomes.length; j++) {
			System.out.println(" - " + nomes[j]);
		}
	}

}
