public class Estrin{
	public static double expoRapide(double x, int n){
		if(n==0){
			return 1.;
		}else{
			double a = expoRapide(x, n/2);
			if(n%2==0){
				return a*a;
			}else{
				return a*a*x;
			}
		}
	}
	static double evalue(double[] p, double al, int i, int j){
		if(i == j){
			return p[i];
		}
		double q = 0;
		q = evalue(p, al, (int) (i+j+1)/2, j)*expoRapide(al, (int) (j-i+1)/2) + evalue(p, al, i, (int) (i+j+1)/2-1);
		return q;
	}
	static double estrin(double[] p, double al){
		return evalue(p, al, 0, p.length-1);
	}

	static double horner(double[] p, double al){
		double res = 0;
		for(int i = 0; i < p.length; i++){
			res *= al;
			res += p[p.length-1-i];
		}
		return res;
	}

	public static void main(String[] args) {
		double[] pol = {1.,2.,3.,4.,5.,6.,7.,8.,9.,10.,11.,12.,13.,14.,15.,16.,17.,18.,19.,20.};
		System.out.println(estrin(pol, -2.));
		System.out.println(horner(pol, -2.));
	}
}
