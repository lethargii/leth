	// Instructions de base
	// Exercice 1
	// 1.
public class instructionsDeBase{
	static int sommeEntiers(int n){
		int res = 0;
		for(int i = 1; i <= n; i++){
			res += i;
		}
		return res;
	}

	// 2.
	static void tableMultiplication(int n){
		for(int i = 0; i <= n; i++){
			System.out.println(i + " x " + n + " = " + i*n);
		}
	}

	// 3.
	static void afficheDiviseur(int n){
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= 10; j++){
				if(i * j == n){
					System.out.println(i);
				}
			}
		}
	}

	// 4.
	static double un(int n){
		double u = 4;
		for(int i = 1; i <= n; i++){
			u = (3 * u + 2)/(u + 7);
		}
		return u;
	}

	// 5.
	static int vn(float eps){
		double v = 1;
		int i = 0;
		while(v < 4-eps | v > 4+eps){
			v = (3 * v + 12)/(v + 2);
			i += 1;
		}
		return i;
	}

	// 6.
	static int Fibonacci(double n){
		int f0 = 0;
		int f1 = 1;
		if(n == 0){
			return f0;
		}
		else if(n == 1){
			return f1;
		}
		else{
			int f = 0;
			for(int i = 2; i <= n; i++){
				f = f0 + f1;
				f0 = f1;
				f1 = f;
			}
			return f;
		}
	}
	public static void main(String[] Args){
		System.out.println("sommeEntiers(4) :");
		System.out.println(sommeEntiers(4));
		System.out.println("tableMultiplication(7) :");
		tableMultiplication(7);
		System.out.println("afficheDiviseur(12) :");
		afficheDiviseur(12);
		System.out.println("un(16) :");
		System.out.println(un(16));
		System.out.println("vn(0.01f) :");
		System.out.println(vn(0.01f));
		System.out.println("Fibonacci(10) :");
		System.out.println(Fibonacci(10));
	}
}
