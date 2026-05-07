package CEP;

import java.util.Scanner;

public class Executor {
	
	public static void main(String[] args) {

		//CRIAÇÃO DE OBJETOS
		
		Scanner leitor = new Scanner(System.in);
		
		Cidade c1 = new Cidade();
		Estado e1 = new Estado();
		Pais p1 = new Pais();
		Politico pc = new Politico();
		Politico pe = new Politico();
		Politico pp = new Politico();
		
		c1.estado = e1;
		c1.prefeito = pc;
		
		e1.pais = p1;
		e1.governador = pe;
		
		p1.presidente = pp;
		
		//LEITURA DE DADOS
		
		System.out.println("-----------LEITURA DE DADOS-----------");
		System.out.println("\nCIDADE\nInforme os dados de sua cidade:\n");
		System.out.print("Nome: ");
		c1.nome = leitor.nextLine();
		System.out.print("População (nº de habitantes): ");
		c1.populacao = Integer.parseInt(leitor.nextLine());
		System.out.print("Estado: ");
		c1.estado.nome = leitor.nextLine();
		System.out.print("Prefeito: ");
		c1.prefeito.nome = leitor.nextLine();
		System.out.print("Partido do prefeito: ");
		c1.prefeito.partido = leitor.nextLine();
		
		System.out.println("\nESTADO\nInforme os dados do estado da sua cidade:\n");
		System.out.print("Sigla: ");
		c1.estado.sigla = leitor.nextLine();
		System.out.print("País: ");
		c1.estado.pais.nome = leitor.nextLine();
		System.out.print("Governador: ");
		c1.estado.governador.nome = leitor.nextLine();
		System.out.print("Partido do governador: ");
		c1.estado.governador.partido = leitor.nextLine();
		
		System.out.println("\nPAÍS\nInforme os dados do estado da sua cidade:\n");
		System.out.print("Continente: ");
		c1.estado.pais.continente = leitor.nextLine();
		System.out.print("Presidente: ");
		c1.estado.pais.presidente.nome = leitor.nextLine();
		System.out.print("Partido do presidente: ");
		c1.estado.pais.presidente.partido = leitor.nextLine();
		
		//IMPRESSÃO
		
		System.out.println("\n-----------IMPRESSÃO-----------");
		System.out.println("\nCIDADE");
		System.out.println("Nome: " + c1.nome);
		System.out.println("População (nº de habitantes): " + c1.populacao);
		System.out.println("Estado: " + c1.estado.nome);
		System.out.println("Prefeito: " + c1.prefeito.nome);
		System.out.println("Partido do prefeito: " + c1.prefeito.partido);
		
		System.out.println("\nESTADO");
		System.out.println("Nome: " + c1.estado.nome);
		System.out.println("Sigla do nome: " + c1.estado.sigla);
		System.out.println("País: " + c1.estado.pais.nome);
		System.out.println("Governador: " + c1.estado.governador.nome);
		System.out.println("Partido do governador: " + c1.estado.governador.partido);
		
		System.out.println("\nPAÍS");
		System.out.println("Nome: " + c1.estado.pais.nome);
		System.out.println("Continente do país: " + c1.estado.pais.continente);
		System.out.println("Presidente: " + c1.estado.pais.presidente.nome);
		System.out.println("Partido do presidente: " + c1.estado.pais.presidente.partido);
		
	
	}
}
