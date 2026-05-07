package moodleStringRandom;

import javax.swing.JOptionPane;

public class M1 {

	public static void main(String[] args) {
		/* Crie um programa que leia 10 Strings do usuário (use JOptionPane) e calcule o tamanho médio
das Strings. O tamanho médio deve ser armazenado em um dado do tipo double (com parte
fracionária). Finalmente, o programa deve mostrar o tamanho médio usando um JoptionPane. */
		
		String[] array = new String[10]; 
		
		int somalength = 0;
		
		for (int i = 0; i < array.length; i++) {
			String t = JOptionPane.showInputDialog("Digite a string " + i + ":");
			array[i] = t;
			somalength += array[i].length();	
		}
		
		double média = (double) somalength/ array.length;
		
		JOptionPane.showMessageDialog(null, "A média de carcteres por frase é de: " + média + ".");
	}

}
