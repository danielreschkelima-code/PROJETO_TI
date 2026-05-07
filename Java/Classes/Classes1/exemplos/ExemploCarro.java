package exemplos;

import java.util.Scanner;

public class ExemploCarro {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in); 
		
		Carro c1 = new Carro();
		
		System.out.println("Informe os dados do carro c1");
		
		System.out.print("\nMarca: ");
		c1.marca = leitor.nextLine();
		
		System.out.print("Modelo: ");
		c1.modelo = leitor.nextLine();
		
		System.out.print("Estado ligado (s/n): ");
		char ligado = leitor.nextLine().charAt(0);
		
		if (ligado == 's' || ligado == 'S') {
			c1.ligado = true;
		} else {
			c1.ligado = false;
		}

		c1.imprimir();
		
		c1.ligar();
		
		c1.desligar();
		
		c1.desligar();
		
		c1.ligar();
		
		c1.acelerar();
		
	}

}
