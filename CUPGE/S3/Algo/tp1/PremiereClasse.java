public class PremiereClasse{
	public PremiereClasse(){
		System.out.println("Coucou");
	}
	static void tableMultiplication(int n){
		for(int i = 0; i <= n; i++){
			System.out.println(i + " x " + n + " = " + i*n);
		}
	}
	static void afficheDiviseur(int n){
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= 10; j++){
				if(i * j == n){
					System.out.println(i);
				}
			}
		}
	}
	public static void main(String[] args){
		System.out.println("tableMultiplication(7) :");
		tableMultiplication(7);
		System.out.println("afficheDiviseur(12) :");
		afficheDiviseur(12);
		System.out.println("tableMultiplication(9) :");
		tableMultiplication(9);
		System.out.println("afficheDiviseur(13) :");
		afficheDiviseur(13);
		System.out.println("tableMultiplication(5) :");
		tableMultiplication(5);
		System.out.println("afficheDiviseur(36) :");
		afficheDiviseur(36);
	}
}
