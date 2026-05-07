package moodle2;

import java.util.Scanner;

public class M1 {

	public static void main(String[] args) {
		/* Crie um programa que compute o n�mero m�dio de alunos por turma. Para tal, leia do teclado o
		n�mero de turmas e o n�mero de alunos em cada turma. Nenhuma turma pode ter mais de 32
		alunos! Se o usu�rio informar que uma turma tem mais de 32 alunos, pergunte novamente.*/
		
		Scanner leitor = new Scanner(System.in);
		
		System.out.println("Informe a quantidade de turmas: ");
		int turmas = Integer.parseInt(leitor.nextLine());
		System.out.println("Informe a quantidade de alunos: ");
		int alunos = Integer.parseInt(leitor.nextLine());
		
		float média = alunos/turmas;
		
		System.out.println("A m�dia de alunos por turma � de " + média +  ".");
	}

}
