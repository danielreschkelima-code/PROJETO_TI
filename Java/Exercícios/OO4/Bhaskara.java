package OO4;

public class Bhaskara {
	
	public double[] calcular(double a, double b, double c) {
		double x1 = (-b + Math.pow(b*b-4*a*c, 0.5))/2*a;
		double x2 = (-b - Math.pow(b*b-4*a*c, 0.5))/2*a;
		double[] raizes = {x1,x2};
		return raizes;
	
	}
}

