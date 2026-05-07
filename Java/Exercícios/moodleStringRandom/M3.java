package moodleStringRandom;

import java.util.Iterator;
import java.util.Random;
import java.util.Scanner;

public class M3 {

	public static void main(String[] args) {
		/* Crie um programa que simule n lan�amentos de uma moeda, cujo resultado pode ser cara ou
		coroa. O valor n deve ser informado via teclado. Ap�s simular os n lan�amentos, informe na tela o
		percentual de resultados cara e de coroa */
		
		Scanner leitor = new Scanner(System.in);
		Random r = new Random();
		
		System.out.print("Informe um n�mero inteiro: ");
		int n = Integer.parseInt(leitor.nextLine());
		
		float cara = 0;
		float coroa = 0;
		
		
		for(int i = 1; i < n; i++) {
			int aleatório = r.nextInt(2);
			
			if (aleatório == 0) {
				cara++;
			} else { 
				coroa++;
			}
			
		}
		
		float total = cara + coroa;
		float percentualcara = cara*100/total;
		float percentualcoroa = coroa*100/total; 
			
		System.out.println("Percentual de cara: " + percentualcara + "%.");
		System.out.println("Percentual de coroa: " + percentualcoroa + "%.");		
		
		
	}

}
