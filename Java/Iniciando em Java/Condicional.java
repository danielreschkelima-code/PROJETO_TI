package exemplos;

public class Condicional {

	public static void main(String[] args) {
		int valor1 = 25;
		int valor2 = 75;
		
		int soma = valor1 + valor2; // sempre definir variável
		int multiplicação = valor1 * valor2;
				
		if(soma >= multiplicação) {
		System.out.println("A soma é maior ou igual a multiplicação!");
		} 
		else {
		System.out.println("A soma é menor que a multiplicação");
		}
	}

}
