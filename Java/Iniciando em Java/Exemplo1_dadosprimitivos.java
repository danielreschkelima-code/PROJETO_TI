package exemplos;

public class Exemplo1_dadosprimitivos {

	public static void main(String[] args) {
		
		//Dados de Números inteiros:
		byte b1 = -128; // byte: números de 8 bits com sinal (-128--127).
		System.out.println(b1);
		
		short s1 = 1000; // short: números de 16 bits com sinal (-32.768--32.767).
		System.out.println(s1);
		
		int i1 = 12345; // int: números inteiros de 32 bits com sinal (-2.147.483.648--2.147.483.647). 
		System.out.println(i1);
		
		long l1 = 123456789; // long: números inteiros de 64 bits com sinal (-9.223.372.036.854.775.808--9.223.372.036.854.775.807).
		System.out.println(l1);
		
		//Dados de Números Reais
		
		float f1 = 3.14f; // float: números de ponto flutuante de 32 bits.
		System.out.println(f1);
		
		double d1 = 123.12345678; // double: números de ponto flutuante de 64 bits.
		System.out.println(d1);
		
		//Dados booleanos (True, False)
		
		boolean b = false; // boolean representa valores lógicos (true e false).
		System.out.println(b);
		
		//Dados de caracteres únicos (não são string)
			
		char c = 'A'; // char armazena um único caractere unicode de 16 bits.
		System.out.println(c);

	
		//STRING (NÃO É UM DADO PRIMITIVO!!!!, e, sim, uma classe).
		
		String campus = "IFRS - Feliz";
		System.out.println(campus);
	}
}


/*A linguagem Python tem uma tipagem dinamica, onde ele se auto define o que seria o seu tipo de vari�vel;
Java é uma linguagem fortemente tipada, onde se deve definir tudo;
A string*/

