package exemplos;

import java.util.Scanner;

public class Exemplo01 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.print("Informe uma opção: ");
		int opção = Integer.parseInt(leitor.nextLine());
		
		/* if (opção == 1) {
		 
		} else if (opção == n...) {
		
		} else {
		
		}
		 */
		
		switch(opção) { // é parecido com um condicional.
			case 1: {
				System.out.println("Um");
				break; // para ele retornar o switch para o "desligado" e reavaliar os case.
			}
			
			case 2: {
				System.out.println("Dois");
				break;
			}
			
			case 3: {
				System.out.println("Três");
				break;
			}
			
			default: {
				System.out.println("Outro número");
			}
			
		}

	}

}
