package exemplos;

import java.util.Scanner;

public class Exemplo04 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		int i = 0;
		do { //a diferença do do e do while é a ordem em que a condição acontece. O do só verifica no final (a primeira vez sempre será executada mesmo que for falsa) e o while no início. Veja ex do while
			System.out.println("-----------------------------");
			System.out.println("[1] Dizer olá!");
			System.out.println("[2] Dizer tchau!");
			System.out.println("[3] Sair");
			System.out.println("-----------------------------");
			
			System.out.println("Informe uma opção: ");
			i = Integer.parseInt(leitor.nextLine());
			
			if(i==1) {
				System.out.println("\nOlá!\n");
			} else if(i==2) {	
				System.out.println("\nTchau\n");
			} else if(i==3) {
				System.out.println("\nFIM!\n");
			} else {
				System.out.println("\nOpção inválida!\n");
			}
			
		} while(i!=3);
		
		
	}
}
