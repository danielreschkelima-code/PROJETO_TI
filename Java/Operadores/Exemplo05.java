package exemplos;

import javax.swing.JOptionPane;

public class Exemplo05 {

	public static void main(String[] args) {
		
		String nome = JOptionPane.showInputDialog("Informe o seu nome: ");
		
		String ola = "Olá, " + nome + "!";
		
		JOptionPane.showMessageDialog(null, ola);
	}

}
