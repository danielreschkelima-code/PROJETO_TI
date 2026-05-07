package OO;

import java.util.Scanner;

public class M5 {

	public static void main(String[] args) {
		
		Potência p1 = new Potência();
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.print("Informe a base a: ");
		long base = Integer.parseInt(leitor.nextLine());
		
		System.out.print("Informe o expoente de a: ");
		int expoente = Integer.parseInt(leitor.nextLine());
		
		System.out.println("\nRESULTADO:");
		System.out.println(p1.potencializar(base,expoente));
	}

}
