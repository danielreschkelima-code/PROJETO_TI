package moodle1;

import java.util.Scanner;

public class M3 {

	public static void main(String[] args) {
		
		/* Crie um programa que calcule e mostre o volume de uma esfera. O raio da esfera será fornecido
pelo usuário através do teclado (tipo de dado double). Pesquisa a fórmula para cálcule de volume
da esfera e considere para PI o valor 3.14159 (tipo de dado double) */
		
		Scanner leitor = new Scanner(System.in);
		
		double raio = Double.parseDouble(leitor.nextLine());
		double volume = 4/3*(3.14159)*(raio*raio*raio);
		
		System.out.println("O volume de uma esfera com raio " + raio + " é de: " + volume + ".");

	}

}
