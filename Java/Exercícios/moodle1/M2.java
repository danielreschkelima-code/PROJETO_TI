package moodle1;

import java.util.Scanner;

public class M2 {

	public static void main(String[] args) {
		// Escreva um programa que lê um número do teclado e que determine se ele é par ou impar.
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.print("Informe o número que será testado: ");
		int n = Integer.parseInt(leitor.nextLine());
		
		int resto = n%2;
		
		if (resto == 0) {
			System.out.println("O número " + n + " é par, pois seu resto é 0");
		}
		else {
			System.out.println("O número " + n + " é ímpar, pois seu resto é diferente de 0 e igual a " + resto + ".");
		}
	}
}
