package exemplos;

public class Testecarro {

	public static void main(String[] args) {
		Carro c1 = new Carro();
		
		// COMO ERA
		//c1.modelo = "Maverick";
		//c1.ano = 1970;
		//
		//System.out.print(c1.modelo);
		//System.out.print(c1.ano);
		
		c1.setModelo("Maverick");
		c1.setAno(10);
		
		System.out.println(c1.getModelo());
		System.out.println(c1.getAno());
		
		Carro c2 = new Carro();
		
		c2.setModelo("Tesla");
		c2.setAno(12);
		
		System.out.println(c2.getModelo());
		System.out.println(c2.getAno());
	
	}

}
