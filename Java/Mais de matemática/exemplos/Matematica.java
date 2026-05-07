package exemplos;

public class Matematica {
	
	public int somar (int a, int b){ // public [void ou int ou float ou string] : tipo de dado que ser� retornado do m�todo. Se for void, o m�todo n�o poder� retornar nada.
		int soma = a + b;
		return soma;
	}
	
	public float subtrair (float a, float b) {
		float diferença = a - b;
		return diferença;
	}
	
	public float multiplicar (float a, float b) {
		float produto = a * b;
		return produto;
	}
	
	public double dividir (double a, double b) {
		double quociente = a/b;
		return quociente;
	}
	
	public long potencializar (long a, int b) {
		int base = (int) a;
		for (int i = 1; i < b; i++) {
			a *= base;
		}
		long produto = a;
		return produto;
	}

}
