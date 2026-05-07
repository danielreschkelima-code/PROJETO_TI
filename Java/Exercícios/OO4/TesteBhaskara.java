package OO4;

import java.util.Scanner;

public class TesteBhaskara {

	public static void main(String[] args) {
		
		/* 2. Crie uma classe chamada Bhaskara contendo atributos que representem os coeficientes a, b e c.
Adicione um método chamado calcular que deve imprimir as raízes da equação (quando houver
apenas uma raiz, imprima o valor apenas uma vez).
Finalmente, crie uma classe chamada TesteBhaskara (contendo o método main) que faça as
seguintes tarefas:
a) Leia do teclado do usuário os valores para os coeficientes;
b) Construa um objeto da classe Bhaskara com os dados lidos no item anterior;
c) Execute o método calcular no objeto criado no item anterior; */
		
		Scanner leitor = new Scanner(System.in);
		Bhaskara b = new Bhaskara();
		
		System.out.println("INFROME OS COEFICIENTES DA EQUAÇÃO DO 2º GRAU");
		System.out.print("a: ");
		double a1 = Double.parseDouble(leitor.nextLine());
		System.out.print("b: ");
		double b1 = Double.parseDouble(leitor.nextLine());
		System.out.print("c: ");
		double c1 = Double.parseDouble(leitor.nextLine());
	
		System.out.println("\nRAÍZES");
		System.out.println("x1 =" + b.calcular(a1,b1,c1)[0]);
		System.out.println("x2 =" + b.calcular(a1,b1,c1)[1]);
		
		
	}

}
