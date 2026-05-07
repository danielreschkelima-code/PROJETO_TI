package exemplos;

public class Carro {
	
	private String modelo;
	private int ano;
	
	public String getModelo() {
		return this.modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
		
	}
	
	public int getAno() {
		return this.ano;
	}
	
	public void setAno(int ano) {
		if(ano > 1900 && ano < 2026) {
			this.ano = ano;
		} else {
			System.out.println("Valor inválido!"); // não recomendado, isso é da parte gráfica: fica difícil de reutilizar
		}
	}
	
}
