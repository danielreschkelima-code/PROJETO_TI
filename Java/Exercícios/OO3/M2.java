package OO3;

import java.util.Scanner;

public class M2 {
	
	public static void main(String[] args) {
		
		/*2. Considere as seguintes classes:
a) Carro, contendo 4 rodas e 1 motor;
b) Roda, contendo o seu tamanho (ex: 14, 15, 16 … 20);
c) Motor, contendo o número de cilindros e a potência (ex: 8 ciclindros e 200 cv).
Associe as classes para construir a classe Carro.
Crie pelo menos 3 objetos desta classe, usando dados lidos do usuário via teclado. */
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("-------------------INFORME AS CARACTERÍSTICAS DOS CARROS-------------------");
		
		// Carro 1
		System.out.println("\n*CARRO 1");
		
		Carro c1 = new Carro();
		Motor m1 = new Motor();
		Rodas r1 = new Rodas();
		c1.motor = m1;
		c1.rodas = r1;
		
		System.out.println("\nMOTOR");
		System.out.print("Quantidade de cilindros: ");
		c1.motor.cilindro = Integer.parseInt(leitor.nextLine());
		System.out.print("Potência (em cavalos): ");
		c1.motor.potencia = Integer.parseInt(leitor.nextLine());
		
		System.out.println("\nRODAS");
		System.out.print("Tamanho dos aros: ");
		c1.rodas.aro = Integer.parseInt(leitor.nextLine());
		
		// Carro 2
		System.out.println("\n*CARRO 2");
		
		Carro c2 = new Carro();
		Motor m2 = new Motor();
		Rodas r2 = new Rodas();
		c2.motor = m2;
		c2.rodas = r2;
		
		System.out.println("\nMOTOR");
		System.out.print("Quantidade de cilindros: ");
		c2.motor.cilindro = Integer.parseInt(leitor.nextLine());
		System.out.print("Potência (em cavalos): ");
		c2.motor.potencia = Integer.parseInt(leitor.nextLine());
		
		System.out.println("\nRODAS");
		System.out.print("Tamanho dos aros: ");
		c2.rodas.aro = Integer.parseInt(leitor.nextLine());
		
		// Carro 3
		System.out.println("\n*CARRO 3");
		
		Carro c3 = new Carro();
		Motor m3 = new Motor();
		Rodas r3 = new Rodas();
		c3.motor = m3;
		c3.rodas = r3;
		
		System.out.println("\nMOTOR");
		System.out.print("Quantidade de cilindros: ");
		c3.motor.cilindro = Integer.parseInt(leitor.nextLine());
		System.out.print("Potência (em cavalos): ");
		c3.motor.potencia = Integer.parseInt(leitor.nextLine());
		
		System.out.println("\nRODAS");
		System.out.print("Tamanho dos aros: ");
		c3.rodas.aro = Integer.parseInt(leitor.nextLine());

		System.out.println("\n-------------------IMPRESSÃO-------------------");
		
		// Carro 1
		System.out.println("\n*CARRO 1");
		System.out.println("\nMOTOR");
		System.out.printf("Quantidade de cilindros: %d", c1.motor.cilindro);
		System.out.printf("%nPotência: %d cavalos", c1.motor.potencia);
		System.out.println("\n\nRODAS");
		System.out.printf("Tamanho do aro: %d", c1.rodas.aro);
		
		// Carro 2
		System.out.println("\n\n*CARRO 2");
		System.out.println("\nMOTOR");
		System.out.printf("Quantidade de cilindros: %d", c2.motor.cilindro);
		System.out.printf("%nPotência: %d cavalos", c2.motor.potencia);
		System.out.println("\n\nRODAS");
		System.out.printf("Tamanho do aro: %d", c2.rodas.aro);
		
		// Carro 3
		System.out.println("\n\n*CARRO 3" );
		System.out.println("\nMOTOR");
		System.out.printf("Quantidade de cilindros: %d", c3.motor.cilindro);
		System.out.printf("%nPotência: %d cavalos", c3.motor.potencia);
		System.out.println("\n\nRODAS");
		System.out.printf("Tamanho do aro: %d", c3.rodas.aro);
	
	}
}


