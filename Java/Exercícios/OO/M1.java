package OO;

import java.util.Scanner;

public class M1 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("CONSTRUÇÃO");
		Country c1 = new Country();
		
		System.out.print("Informe o nome do país: ");
		c1.nome = leitor.nextLine();
		System.out.print("Informe a capital do país: ");
		c1.capital = leitor.nextLine();
		System.out.print("Informe o número de habitantes do país: ");
		c1.habitantes = Integer.parseInt(leitor.nextLine());
		
		leitor.close();

		System.out.println("\nIMPRESSÃO");
		
		System.out.printf("Nome: %s", c1.nome);
		System.out.printf("%nCapital: %s", c1.capital);
		System.out.printf("%nNúmero de habitantes: %d", c1.habitantes);
	}

}
