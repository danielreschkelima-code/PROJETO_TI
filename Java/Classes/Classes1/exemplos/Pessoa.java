package exemplos;

public class Pessoa {
	public String nome;
	public String sobrenome;
	public int idade;
	public double altura;
	public boolean vivo;
	
	public void nascer(String nome, String sobrenome, double altura) {
		this.nome = nome;
		this.sobrenome = sobrenome;
		this.altura = altura;
		this.idade = 0;
		this.vivo = true; 
	}
	
	public void matar() {
		this.vivo = false;
	}
	
	public void imprimir() {
		System.out.println("---------------------");
		System.out.println(this.nome);
		System.out.println(this.sobrenome);
		System.out.println(this.idade);
		System.out.println(this.altura);
		System.out.println(this.vivo);
	}
	
	public void falar(String frase) {
		if (this.vivo) {
			System.out.println("---------------------");
			System.out.printf("%s falou: %s%n", this.nome, frase);
		} else {
			System.out.println("A pessoa está morta e não pode falar, por enquanto...");
		}
	}
	
	public void aniversariar() {
		if (this.vivo) {
			this.idade++;
		} else {
			System.out.println("A pessoa está morta; não pôde aniversariar.");
		}
	}

}
