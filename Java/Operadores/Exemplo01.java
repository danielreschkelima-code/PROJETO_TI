package exemplos;

import java.util.Scanner;

public class Exemplo01 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.print("Informe um número: ");
		int n = Integer.parseInt(leitor.nextLine());
		
		System.out.print("Informe outro número: ");
		int m = Integer.parseInt(leitor.nextLine());
		
		if(n == m) {
			System.out.println("Iguais.");
		}
		
		if (n != m) { // o correto seria ser else
			System.out.println("Diferentes:");
		}
	
		if(n > m) {
			System.out.println("n é maior que m.");
		}
		
		else if (n < m) {
			System.out.println("n é menor que m");
		}
		
		// aqui está repetitivo por fins pedagógicos (se n = m, então logicamente também é >=). 
		
		else if (n >= m) {
			System.out.println("n é maior ou igual a m");
		}
		
		else {
			System.out.println("n é menor ou igual a m");
		}
	}
}
