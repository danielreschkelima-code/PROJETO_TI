package exemplos;

import java.util.Scanner;

public class Exemplo04 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe um double: ");
		double d = Double.parseDouble(leitor.nextLine());
		
		// Math
		System.out.println(Math.PI);
		System.out.println(Math.abs(d));
		System.out.println(Math.pow(2, 3));
		System.out.println(Math.sqrt(16));
		System.out.println(Math.pow(16, 0.5));
		
		double v1 = Math.round(d);
		System.out.println(v1);
		
		System.out.println(Math.ceil(d));
		System.out.println(Math.floor(d));
		
		int min = Math.min(10, 20);
		System.out.println(min);
		
		int max = Math.max(30000, 567);
		System.out.println(max);
		
	}

}
