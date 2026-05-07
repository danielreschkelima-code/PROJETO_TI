package exemplos;

public class Exemplowhileedo {

	public static void main(String[] args) {
			
			int i = 10;
			do { //a diferença do do e do while é a ordem em que a condição acontece. O do só verifica no final (a primeira vez sempre será executada mesmo que for falsa) e o while no início. Veja ex do while
				System.out.print(i + " ");
				i++;
			} while(i<5); // este printa o 10.
			
			while(i<5) { // este não printa.
				System.out.println(i + " ");
				i++;
			}
	}
}
