package exemplos;
import java.util.Scanner; // input sempre antes do class e depois do package

public class Input {
	
	
	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		
		// leitor de int.
		System.out.print("Digite um numero: ");
		int valor = Integer.parseInt(leitor.nextLine());
		System.out.println("O valor digitado foi " + valor);
		
		// leitor de ponto flutuante.
		System.out.print("Digite um numero com ponto flutuante: ");
		double valor1 = Double.parseDouble(leitor.nextLine());
		System.out.println("O valor digitado foi " +  valor1);
	
		// leitor de string (lembrando que string não é dado primitivo, e, sim, classe.
		System.out.print("Digite uma palavra: ");
		String palavra = leitor.nextLine();
		System.out.println("A palavra digitada foi " + palavra);
		
		leitor.close(); // fechar leitor depois do último input
	}
}

