package exemplos;

import java.util.Scanner;

public class Exemplo03 {

	public static void main(String[] args) {
		
Scanner leitor = new Scanner(System.in);
		
		System.out.print("Informe um número: ");
		int n = Integer.parseInt(leitor.nextLine());
		
		System.out.print("Informe outro número: ");
		int m = Integer.parseInt(leitor.nextLine());
		
		int soma = n + m;
		System.out.println("Soma: " + soma);
		
		int sub = n - m;
		System.out.println("Subtração: " + sub);
		
		int mult = n * m;
		System.out.println("Multiplicação: " + mult);
		
		int div = n/m;
		System.out.println("Divisão: " + div);
		
		int resto = n % m;
		System.out.println("Resto: " + resto);
	}

}
