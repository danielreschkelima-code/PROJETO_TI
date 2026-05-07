package OO;

public class Potência {
	
	public long potencializar (long a, int b) {
		int base = (int) a;
		
		if (b>0) {
			for (int i = 1; i < b; i++) {
				a *= base;
			}
		long produto = a;
		return produto;
		} else if (b == 0){
			long produto = 1;
			return produto;
		} else {
			for (int i = 1; i < b; i++) {
				a *= base;
			}
			long produto = 1/a;
			return produto;
		}
	}
}
