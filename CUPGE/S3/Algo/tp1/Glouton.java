public class Glouton{
	public static boolean verifieSysteme(int[] tab){
		if(tab[tab.length - 1] != 1){
			return false;
		}
		for(int i = 0; i < tab.length - 1; i++){
			if(tab[i] <= tab[i + 1]){
				return false;
			}
		}
		return true;
	}

	public static int[] rend(int x, int[] c){
		int[] res = new int[c.length];
		int i = 0;
		while(x > 0){
			if(c[i] > x){
				i++;
			}
			else{
				x -= c[i];
				res[i] += 1;
				i = 0;
			}
		}
		return res;
	}

	public static int cardinal(boolean[] ens){
		int res = 0;
		for(boolean el: ens){
			if(el){
				res += 1;
			}
		}
		return res;
	}

	public static boolean[] tabVersEns(int[] tab, int maxi){
		boolean[] res = new boolean[maxi + 1];
		for(int el: tab){
			res[el] = true;
		}
		return res;
	}

	public static int[] ensVersTab(boolean[] ens){
		int length = 0;
		for(boolean el: ens){
			if(el){
				length += 1;
			}
		}
		int[] tab = new int[length];
		int j = 0;
		for(int i = 0; i < ens.length; i++){
			if(ens[i]){
				tab[j] = i;
				j++;
			}
		}
		return tab;
	}

	public static boolean[] diff(boolean[] ens1, boolean[] ens2){
		boolean[] ens3 = new boolean[ens1.length];
		for(int i = 0; i < ens1.length; i++){
			if(ens1[i] && !ens2[i]){
				ens3[i] = true;
			}
		}
		return ens3;
	}

	public static boolean nonVide(boolean[] ens){
		for(boolean el: ens){
			if(el){
				return true;
			}
		}
		return false;
	}

	public static boolean[] ensRestants(boolean[] ensEleves, boolean[] act){
		return diff(ensEleves, act);
	}

	public static int nbreRestants(boolean[] ensEleves, boolean[] act){
		return cardinal(ensRestants(ensEleves, act));
	}

	public static int meilleureActivite(boolean[][] acts, boolean[] ensEleves){
		int indiceMini = 0;
		int mini = nbreRestants(ensEleves, acts[0]);
		for(int i = 1; i < acts.length; i++){
			if(nbreRestants(ensEleves, acts[i]) < mini){
				mini = nbreRestants(ensEleves, acts[i]);
				indiceMini = i;
			}
		}
		return indiceMini;
	}

	public static boolean couvre(boolean[] ensActs, boolean[][] acts){
		boolean interesse;
		for(int i = 0; i < acts[0].length; i++){
			interesse = false; 
			for(int j = 0; j < acts.length; j++){
				if(ensActs[j] && acts[j][i]){
					interesse = true;
				}
			}
			if(!interesse){
				return false;
			}
		}
		return true;
	}

	public static boolean[] glouton(boolean[][] acts){
		boolean[] ensEleves = new boolean[acts[0].length];
		for(int i = 0; i < ensEleves.length; i++){
			ensEleves[i] = true;
		}
		boolean[] ensActs = new boolean[acts.length];
		int indiceMeilleureActivite;
		while(!couvre(ensActs, acts)){
			indiceMeilleureActivite = meilleureActivite(acts, ensEleves);
			ensActs[indiceMeilleureActivite] = true;
			for(int i = 0; i < acts[indiceMeilleureActivite].length; i++){
				if(acts[indiceMeilleureActivite][i]){
					ensEleves[i] = false;
				}
			}
		}
		return ensActs;
	}

	public static boolean[] optimale(boolean[][] acts){
		boolean[] ensActsOpt = new boolean[acts.length];
		boolean[] ensActs = new boolean[acts.length];
		for(int i = 0; i < Math.pow(ensActs.length, 2)-1; i++){
			boolean retenue = true;
			int j = 0;
			while(retenue){
				if(!ensActs[j]){
					retenue = false;
				}
				ensActs[j] = !ensActs[j];
				j++;
			}
			if(couvre(ensActs,acts) && (cardinal(ensActs) < cardinal(ensActsOpt) || cardinal(ensActsOpt) == 0)){
				for(int k = 0; k < ensActs.length; k++){
					ensActsOpt[k] = ensActs[k];
				}
			}
		}
		return ensActsOpt;
	}

	public static void main(String[] args){
		//8.1
		System.out.println("8.1");
		int[] tab1 = {200,100,50,20,10,5,2,1};
		System.out.println(verifieSysteme(tab1));
		int[] tab2 = {200,100,50,20,10,5,2};
		System.out.println(verifieSysteme(tab2));
		int[] tab3 = {200,100,50,20,10,2,2,1};
		System.out.println(verifieSysteme(tab3));
		System.out.println();
		//8.2
		System.out.println("8.2");
		Tableaux.afficheTab(rend(64,tab1));
		System.out.println("La complexité de rend est de O(n), n étant la longueur du tableau.");
		System.out.println();
		//8.3
		System.out.println("8.3");
		System.out.println("Avec cet algorithme glouton, on rendrait une pièce de 30, une pièce de 12 et une pièce de 6, ce qui fait une total de 3 pièces. Or, on peut rendre seulement 2 pièces de 24.");
		System.out.println();
		//9.1
		System.out.println("9.1");
		boolean[] ens = {true, false, false, true, true, false};
		System.out.println(cardinal(ens));
		System.out.println("La complexité de cardinal est de O(n), n étant la longeur de ens");
		System.out.println();
		//9.2
		System.out.println("9.2");
		int[] tab = {1, 5, 6, 8};
		System.out.println("tabVersEns([1, 5, 6, 8],9) : ");
		Tableaux.afficheTab(tabVersEns(tab, 9));
		System.out.println("ensVersTab([false, true, false, false, false, true, true, false, true, false],9) : ");
		Tableaux.afficheTab(ensVersTab(tabVersEns(tab, 9)));
		System.out.println("La complexité de tabVersEns est de O(n), n étant la longueur de tab.");
		System.out.println("La complexité de ensVersTab est de O(n), n étant la longueur de ens.");
		System.out.println();
		//9.3
		System.out.println("9.3");
		boolean[] ens1 = {false, true, false, true, false, true};
		boolean[] ens2 = {true, true, false, false, false, true};
		System.out.println("diff([false, true, false, true, false, true], [true, true, false, false, false, true]) : ");
		Tableaux.afficheTab(diff(ens1,ens2));
		System.out.println("La complexité de diff est de O(n), n étant la longueur de ens1 et ens2.");
		System.out.println();
		//9.4
		System.out.println("9.4");
		boolean[] ens3 = {false, false, false, false, false, false};
		System.out.println("nonVide([true, true, false, false, false, true]) :" + nonVide(ens2));
		System.out.println("nonVide([false,false, false, false, false, false]) :" + nonVide(ens3));
		System.out.println("La complexité de nonVide est de O(n), n étant la longueur de ens.");
		System.out.println();
		//9.5
		System.out.println("9.5");
		System.out.println("ensRestants([false, true, false, true, false, true],[true, true, false, false, false, true]) : ");
		Tableaux.afficheTab(ensRestants(ens1,ens2));
		System.out.println("La complexité de ensRestants est de O(n), n étant la longueur de ensEleves et act.");
		System.out.println();
		//9.6
		System.out.println("9.6");
		System.out.println("nbreRestants([false, true, false, true, false, true],[true, true, false, false, false, true]) : " + nbreRestants(ens1, ens2));
		System.out.println("La complexité de nbreRestants est de O(n), n étant la longueur de ensEleves et act.");
		System.out.println();
		//9.7
		System.out.println("9.7");
		boolean[][] acts0 = {{true, true, true, false, false, false, false},
		{false, true, false, true, false, false, false},
		{true, false, true, false, true, false, true},
		{false, false, false, true, false, true, false},
		{true, false, false, true, false, false, true}};
		boolean[] ens4 = {false, false, false, true, false, true, false};
		System.out.println("meilleureActivite(acts0,[false,false,false,true,false,true,false]) : " + meilleureActivite(acts0, ens4));
		System.out.println("La complexité de meilleureActivite est de O(n*m), n étant la longueur de ensEleves et m étant la longueur de acts.");
		System.out.println();
		//9.8
		System.out.println("9.8");
		boolean[] ens5 = {false, false, true, false, true};
		boolean[] ens6 = {true, true, true, true, false};
		System.out.println("couvre([false,false,true,false,true],acts0) : " + couvre(ens5, acts0));
		System.out.println("couvre([true,true,true,true,false],acts0) : " + couvre(ens6, acts0));
		System.out.println();
		//9.9
		System.out.println("9.9");
		System.out.println("L'ensemble des activités sélectionnées par l'algorithme glouton si l'ensemble des activités est acts0 est [false, true, true, true, false]");
		System.out.println();
		//9.10
		System.out.println("9.10");
		System.out.println("glouton(acts0) : ");
		Tableaux.afficheTab(glouton(acts0));
		System.out.println();
		//9.11
		System.out.println("9.11");
		System.out.println("L'algorithme renvoie une solution non idéal si par exemple acts1=\n[[false, true, false, true, false, true],\n[true, true, false, false, false, false],\n[false, false, true, true, false, false],\n[false, false, false, false, true, true]]");
		System.out.println();
		//9.12
		System.out.println("9.12");
		boolean[][] acts1 = {{false, true, false, true, false, true},
		{true, true, false, false, false, false},
		{false, false, true, true, false, false},
		{false, false, false, false, true, true}};
		Tableaux.afficheTab(glouton(acts1));
		Tableaux.afficheTab(optimale(acts1));
		System.out.println();
	}
}
