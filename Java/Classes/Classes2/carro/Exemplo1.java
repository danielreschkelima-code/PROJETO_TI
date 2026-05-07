package carro;

public class Exemplo1 {

	public static void main(String[] args) {

		Motor m1 = new Motor();
		m1.litragem = 2;
		m1.cilindro = 4;
		m1.injeçaoDireta = false;
		
		// Não preciso mais de m1, pois m1 está associoado a m1.
		
		Carro c1 = new Carro();
		c1.fabricante = "Chevrolet";
		c1.modelo = "Renegade";
		c1.motor = m1;
		
		System.out.println("--------IMPRESSÃO--------");
		System.out.println("Fabricante: " + c1.fabricante);
		System.out.println("Modelo: " + c1.modelo);
		System.out.println("Litragem do motor: " + c1.motor.litragem);
		System.out.println("Cilindro do motor: " + c1.motor.cilindro);
		System.out.println("Injeção Direta do motor: " + c1.motor.injeçaoDireta);
		
	}

}
