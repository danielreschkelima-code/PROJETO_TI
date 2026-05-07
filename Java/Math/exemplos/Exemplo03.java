package exemplos;

import java.util.Scanner;

public class Exemplo03 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe um número: ");
		int i = Integer.parseInt(leitor.nextLine());
		
		float f1 = i;
		double d1 = i;
		
		System.out.println(i);
		System.out.println(f1);
		System.out.println(d1);
		
		System.out.println("-----------------------");
		
		System.out.println("Informe um double: ");
		double d = Double.parseDouble(leitor.nextLine());
		
		int i1 = (int) d;
		long l1 = (long) d;
		
		System.out.println(d);
		System.out.println(i1);
		System.out.println(l1);
		
		System.out.println("-----------------------");
		
		int c = 100;
		
		double m = ((double) c)/3;
		System.out.println(m);
		
	}

}
