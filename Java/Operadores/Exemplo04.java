package exemplos;

import java.util.Scanner;

public class Exemplo04 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.print("Informe um número: ");
		double n = Double.parseDouble(leitor.nextLine());
		
		System.out.print("Informe outro número: ");
		double m = Double.parseDouble(leitor.nextLine());
		
		double soma = n + m;
		System.out.println("Soma: " + soma);
		
		double sub = n - m;
		System.out.println("Subtração: " + sub);
		
		double mult = n * m;
		System.out.println("Multiplicação: " + mult);
		
		double div = n/m;
		System.out.println("Divisão: " + div);
		
		double resto = n % m;
		System.out.println("Resto: " + resto);
	}
}

