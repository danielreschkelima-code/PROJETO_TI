package geteset;

import java.util.Scanner;

public class Testeanimal {

	public static void main(String[] args) {
			
		System.out.println("GERADOR DE ANIMAIS");
		
		Scanner leitor = new Scanner(System.in);
		Animal a1 = new Animal();
		
		System.out.println("\nLEITURA");
		System.out.print("Nome do animal: ");
		String nome = leitor.nextLine();
		a1.setNome(nome);
		System.out.print("Espécie do animal: ");
		String especie = leitor.nextLine();
		a1.setEspecie(especie);
		
		System.out.println("\nIMPRESSÃO");
		System.out.println("Nome do animal: " + a1.getNome());
		System.out.println("Espécie do animal: " + a1.getEspecie());
		
	}

}
