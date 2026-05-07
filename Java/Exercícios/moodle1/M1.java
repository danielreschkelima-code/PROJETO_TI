package moodle1;

import java.util.Scanner;

public class M1 {

	public static void main(String[] args) {
		
		// 1. Faça um programa que leia 2 números inteiros do teclado e que imprima na tela a soma,
		// substração, multiplicação, divisão e resto da divisão desses dois números.
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.print("Digite um número: ");
		int a = Integer.parseInt(leitor.nextLine());
				
		System.out.print("Digite outro número: ");
		int b = Integer.parseInt(leitor.nextLine());
		
		int soma = a + b;
		System.out.println("Soma: " + soma);
		
		int sub = a - b;
		System.out.println("Subtração: " + sub);
		
		int mult = a * b;
		System.out.println("Multiplicação: " + mult);
		
		double div = a/b;
		System.out.println("Divisão: " + div);
		
		int resto = a % b;
		System.out.println("Resto: " + resto);
	}

}
