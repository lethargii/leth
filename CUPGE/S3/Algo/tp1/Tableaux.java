public class Tableaux{
	public static void afficheTab(int[] tab){
		System.out.print("[");
		for(int i = 0; i < tab.length - 1; i++){
			System.out.print(tab[i] + ", ");
		}
		if(tab.length > 0){
			System.out.print(tab[tab.length - 1]);
		}
		System.out.println("]");
	}

	public static void afficheTab(boolean[] tab){
		System.out.print("[");
		for(int i = 0; i < tab.length - 1; i++){
			System.out.print(tab[i] + ", ");
		}
		if(tab.length > 0){
			System.out.print(tab[tab.length - 1]);
		}
		System.out.println("]");
	}
}
