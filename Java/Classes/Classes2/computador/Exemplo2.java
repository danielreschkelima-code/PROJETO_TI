package computador;

import java.util.Scanner;

public class Exemplo2 {

	public static void main(String[] args) {
		
		Scanner leitor = new Scanner(System.in);
		Computador c1 = new Computador();
		Placamae p1 = new Placamae();
		Processador cpu1 = new Processador();
		c1.placamae = p1;
		c1.processador = cpu1;
		
		
		
		System.out.println("----------------------RESGATE DE INFORMAÇÕES----------------------");
		
		System.out.println("\nPLACA MÃE");
		System.out.print("Informe o modelo da placa mãe: ");
		p1.modelo = leitor.nextLine();
		System.out.print("Informe o fabricante da placa mãe: ");
		p1.fabricante = leitor.nextLine();
		System.out.print("Informe o chipset da placa mãe: ");
		p1.chipset = leitor.nextLine();
		
		System.out.println("\nPROCESSADOR");
		System.out.print("Informe o modelo do processador: ");
		cpu1.modelo = leitor.nextLine();
		System.out.print("Informe o fabricante do processador: ");
		cpu1.fabricante = leitor.nextLine();
		System.out.print("Informe a frequência média em Ghz do processador: ");
		cpu1.frequenciamedia = Float.parseFloat(leitor.nextLine());
		
		System.out.println("\nCOMPUTADOR");
		System.out.print("Informe se o computador é um desktop(true) ou não (false): ");
		c1.desktop = Boolean.parseBoolean(leitor.nextLine());
		
		System.out.println("\n----------------------IMPRESSÃO----------------------");
		
		System.out.println("\nINFORMAÇÕES DO COMPUTADOR");
		System.out.println("Desktop: " + c1.desktop);
		System.out.println("Placa mãe: " + c1.placamae.modelo);
		System.out.println("Processador: " + c1.processador.modelo);
		
		System.out.println("\nINFORMAÇÕES DA PLACA MÃE");
		System.out.println("Modelo: " + p1.modelo);
		System.out.println("Fabricante: " + p1.fabricante);
		System.out.println("Chipset: " + p1.chipset);
		
		
		System.out.println("\nINFORMAÇÕES DO PROCESSADOR");
		System.out.println("Modelo: " + cpu1.modelo);
		System.out.println("Fabricante: " + cpu1.fabricante);
		System.out.println("Frequência: " + cpu1.frequenciamedia + " GHz");
		
	}

}
