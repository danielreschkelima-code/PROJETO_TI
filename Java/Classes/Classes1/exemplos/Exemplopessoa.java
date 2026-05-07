package exemplos;

public class Exemplopessoa {

	public static void main(String[] args) {
		
		Pessoa p1 = new Pessoa();
		
		p1.nome = "Sabrina";
		p1.sobrenome = "Amorosa";
		p1.idade = 14;
		p1.altura = 1.75;
		
		p1.imprimir();
		
		Pessoa p2 = new Pessoa();
		p2.nome = "Norman";
		p2.sobrenome = "Xereta";
		p2.idade = 64;
		p2.altura = 1.6;
		
		p2.imprimir();
		
		p1.falar("Não.");
		p2.falar("Essa geração de hoje em dia... Perdidos!");
		
		p1.aniversariar();
		
		p1.imprimir();
		
		Pessoa p3 = new Pessoa();
		p3.nascer("Maria", "Linda", 0.4);
		
		for (int i = 0; i<35; i++) {
			p3.aniversariar();
		}
		
		p3.altura = 1.67;
		
		p3.imprimir();
		
		for (int i = 0; i<45; i++) {
			p3.aniversariar();
		}	
		
		p3.matar();
		p3.falar("Voltei dos mortos");
		
	}
}
