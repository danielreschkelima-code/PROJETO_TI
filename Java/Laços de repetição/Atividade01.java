package exemplos;

import java.util.Scanner;

public class Atividade01 {

	public static void main (String[] args ) {
	
	//Ler um número n do teclado e imprimir os múltiplos de 3 entre 0 e n.
	Scanner leitor = new Scanner(System.in);
	
	System.out.println("Informe um nýmero: ");
	int n = Integer.parseInt(leitor.nextLine());
	
	int i = 3;
			
	while(i<=n) {
		System.out.println(i + " ");
		i += 3;
		
	}
		
	}
}
