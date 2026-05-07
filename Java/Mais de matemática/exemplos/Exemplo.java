package exemplos;

public class Exemplo {

	public static void main(String[] args) {
		// Scanner
		// Criar m�todos subtrair, multiplicar e dividir
		
		Matematica m1 = new Matematica();
			
		System.out.println("CONTAS\n");
		System.out.println("A soma de 10 + 10 �: " + m1.somar(10,10) + ".");
		System.out.println("A diferen�a de 10 - 10 �: " + m1.subtrair(10,10) + ".");
		System.out.println("O produto de 10 * 10 �: " + m1.multiplicar(10,10) + ".");
		System.out.println("O quociente de 10/10 �: " + m1.dividir(10,10) + ".");
		System.out.println("A pot�ncia de 10^10 �: " + m1.potencializar(10,-1) + ".");

	}

}
