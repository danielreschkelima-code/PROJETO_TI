package moodleStringRandom;

import java.util.Scanner;

public class M2 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		String palavra1 = "";
		boolean bandeira = true; 
		while(bandeira == true) {
			System.out.println("Informe a primeira string (de 10 caracteres): ");
			palavra1 = leitor.nextLine();
			if (palavra1.length() != 10 ){
				System.out.println("Com exatamente 10 caracteres: ");
				 palavra1 = leitor.nextLine();
			} else {
				bandeira = false;
			}
		}
		
		System.out.println();
		
		String palavra2 = "";
		bandeira = true; 
		while(bandeira == true) {
			System.out.println("Informe a segunda string (de 10 caracteres): ");
			palavra2 = leitor.nextLine();
			if (palavra2.length() != 10 ){
				System.out.println("Com exatamente 10 caracteres: ");
				 palavra2 = leitor.nextLine();
			} else {
				bandeira = false;
			}
		}
		
		int iguais = 0;
		
		for (int i = 0; i < (palavra1.length()); i++) {
			if (palavra1.charAt(i) == palavra2.charAt(i)) {
				iguais++;
			}
		}
		
		int diferentes = palavra1.length() - iguais;	
		double similaridade = (double) iguais*100 / palavra1.length();
		
		System.out.println();
		System.out.println("A similaridade de caracteres é de: " + similaridade + "%.");		
	}

}
