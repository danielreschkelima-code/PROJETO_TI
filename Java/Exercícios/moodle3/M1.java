package moodle3;

import java.util.Scanner;

public class M1 {

	public static void main(String[] args) {
		/* Crie um programa Java que contenha um array de 10 números criados por você.
		Imprima na tela os valores do array precedidos pelo seu respectivo índice. */
		
		Scanner leitor = new Scanner(System.in);
		
		int números[] = new int[10];
		
		System.out.println("INFORME OS NÚMEROS DAS POSIÇÕES...\n" );
		
		for (int i = 0; i < números.length; i++) {
			System.out.print("Posição " + i + ": ");
			números[i] = Integer.parseInt(leitor.nextLine());
		}
		
		System.out.println("\nLISTA DIGITADA: " );
		
		for (int i = 0; i < números.length; i++) {
			System.out.println("Posição " + i + ": " + números[i]);
		}
	}

}
