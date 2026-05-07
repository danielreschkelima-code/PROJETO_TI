package moodle2;

import java.util.Scanner;

public class M2 {

	public static void main(String[] args) {
		/*Fa�a um programa que pe�a um n�mero inteiro e determine se ele � ou n�o um n�mero primo.
Um n�mero primo � aquele que � divis�vel somente por ele mesmo e por 1. */
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe um número para saber se ele é primo ou não: ");
		int entrada = Integer.parseInt(leitor.nextLine());
		
		boolean primo = true;

		if (entrada<2) {
			System.out.println(entrada + " não é primo.");
		} else if (entrada == 2) {
			System.out.println(entrada + " é primo");
		} else {
			for (int i=3; i<entrada ; i++){
				float resto = entrada%i;
				
				if(resto == 0 && entrada != i){
					primo = !primo;
					break;
					}
			}
		}
		
		if (primo==true) {
			System.out.println(entrada + " é primo.");
		} else {
			System.out.println(entrada + " não é primo.");
		}	
	}

}

