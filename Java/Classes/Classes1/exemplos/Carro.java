package exemplos;

public class Carro {
	public String marca;
	public String modelo;
	public boolean ligado;


	public void imprimir() {
		System.out.println("\n---------------------");
		System.out.println("DADOS CARRO " + this.modelo);
		System.out.println("Marca: " + this.marca);
		System.out.println("Modelo: " + this.modelo);
		System.out.println("Estado ligado: " + this.ligado);
	}
	
	public void ligar() {
		if (this.ligado) {
			System.out.println("\nO carro " + this.modelo + " já está ligado.");
		} else {
			this.ligado = !this.ligado;
		}
	}
	
	public void desligar() {
		if (this.ligado == false) {
			System.out.println("\nO carro " + this.modelo + " já está desligado.");
		} else {
			this.ligado = !this.ligado;
		}
	}
	
	public void acelerar() {
		if (this.ligado == false) {
			System.out.println("\nO carro está desligado e não pode acelerar");
		} else {
			System.out.println("\nTurbo!");
		}
	}

}