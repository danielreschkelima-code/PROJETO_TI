package moodle3;

import java.util.Scanner;

public class M5 {

	public static void main(String[] args) {
		
		/* Crie um programa Java que:
a) Leia 5 valores inteiros do teclado e armazene-os em um array.
b) Após armazenar os valores no array, faça a contagem de quantos valores são negativos.
c) Finalmente, mostre os valores positivos na tela*/
		
		Scanner leitor = new Scanner(System.in);
		
		int[] array = new int[5];
		
		System.out.println("PREENCHA AS POSIÇÕES DO ARRAY...");
		
		for (int i = 0; i < array.length; i++) {
			System.out.print("Posição " + i + ": ");
			array[i] = Integer.parseInt(leitor.nextLine());
		}
		
		int negativos = 0;
		
		for (int i = 0; i < array.length; i++) {
			if (array[i]< 0){
				negativos++;
			}
		}
		int positivosounulos = 5 - negativos;
		
		System.out.println("\nOS VALORES POSITIVOS OU NULOS SÃO " + positivosounulos + ":");
		
		for (int i = 0; i < array.length; i++) {
			if (array[i]>=0){
				System.out.println(array[i]);
			}
		}
	}

}
