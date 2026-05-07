package exemplos;

import java.util.Scanner;

public class Exemplo02 {

	public static void main(String[] args) {


		Scanner leitor = new Scanner(System.in);

		System.out.print("Informe um número: ");
		int n = Integer.parseInt(leitor.nextLine());

		System.out.print("Informe outro número: ");
		int m = Integer.parseInt(leitor.nextLine());

		// AND (E) &&

		if ((n==0) && (m==0)) {
			System.out.println("Ambos são zero!");
		}

		// OR (ou) ||

		if ((n==10) || (m==10)) {
			System.out.println("Pelo menos um é igual a 10!");
		}

		// Not (não) !

		boolean flag = true;

		if (!flag== false) {
			System.out.println("false");
		}
	}
}