import java.util.ArrayList;
import java.util.Arrays;

public class Plsssc{
	public static int longueurPlsssc(int[] tab){
		int[] tabLong = new int[tab.length];
		tabLong[0] = 1;
		for(int i = 1; i < tabLong.length; i++){
			int max_prec = 0;
			for(int j = 1; j < i; j++){
				if(tab[j] < tab[i]){
					max_prec = Math.max(max_prec, tabLong[j]);
				}
			}
			tabLong[i] = 1 + max_prec;
		}
		int longueur = 0;
		for(int i = 0; i < tabLong.length; i++){
			longueur = Math.max(longueur, tabLong[i]);
		}
		return longueur;
	}
	public static int[] plsssc(int[] tab){
		int[] tabLong = new int[tab.length];
		int[] prec = new int[tab.length];
		tabLong[0] = 1;
		for(int i = 1; i < tabLong.length; i++){
			int maxPrec = 0;
			int indexMaxPrec = -1;
			for(int j = 0; j < i; j++){
				if(tab[j] < tab[i]){
					maxPrec = Math.max(maxPrec, tabLong[j]);
					indexMaxPrec = j;
				}
			}
			tabLong[i] = 1 + maxPrec;
			prec[i] = indexMaxPrec;
		}
		int index = 0;
		for(int i = 0; i < tabLong.length; i++){
			if(tabLong[i] > tabLong[index]){
				index = i;
			}
		}
		int[] res = new int[tabLong[index]];
		for(int i = tabLong[index]; i >= 0; i++){
			res[i-1] = tab[index];
			index = prec[index];
		}
		return res;
	}
	public static void main(String[] args){
		int[] tab = {0, 11, 11, 0, 11, 8, 2, 3, 7, 2, 7, 3, 13, 9, 6, 12, 9, 8, 7, 5};
		System.out.println(longueurPlsssc(tab));
		System.out.println(plsssc(tab));
	}
}
