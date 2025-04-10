public class ABR{
	int cle;
	int valeur;
	ABR filsGauche;
	ABR filsDroit;
	public ABR(int cle, int valeur, ABR filsGauche, ABR filsDroit){
		this.cle = cle;
		this.valeur = valeur;
		this.filsGauche = filsGauche;
		this.filsDroit = filsDroit;
	}
	public static int[] sousTableau(int[] tab, int i, int j){
		int[] res = new int[j-i+1];
		for(int k = 0; k < res.length; k++){
			res[k] = tab[k+i];
		}
		return res;
	}
	public ABR(int[] tab_cles, int[] tab_valeurs){
		if(tab_cles.length == 2){
			cle = tab_cles[0];
			valeur = tab_valeurs[0];
			filsGauche = null;
			filsDroit = new ABR(tab_cles[1], tab_valeurs[1], null, null);
		}
		else if(tab_cles.length == 1){
			cle = tab_cles[0];
			valeur = tab_valeurs[0];
			filsGauche = null;
			filsDroit = null;
		}
		else{
			int m = (int) (tab_cles.length-1)/2;
			cle = tab_cles[m];
			valeur = tab_valeurs[m];
			filsGauche = new ABR(sousTableau(tab_cles, 0, m-1), sousTableau(tab_valeurs, 0, m-1));
			filsDroit = new ABR(sousTableau(tab_cles, m+1, tab_cles.length-1), sousTableau(tab_valeurs, m+1, tab_valeurs.length-1));
		}
	}
	public boolean appartient(int c){
		if(cle == c){
			return true;
		}
		if(c < cle && filsGauche != null && filsGauche.appartient(c)){
			return true;
		}
		else if(filsDroit != null){
			return filsDroit.appartient(c);
		}
		return false;
	}
	public int getValeur(int c){
		if(cle == c){
			return valeur;
		}
		if(c < cle && filsGauche != null){
			return filsGauche.getValeur(c);
		}
		if(filsDroit != null){
			return filsDroit.getValeur(c);
		}
		return 0;
	}
	public void insert(int c, int v){
		if(c < cle){
			if(filsGauche != null){
				filsGauche.insert(c, v);
			}
			else{
				filsGauche = new ABR(c, v, null, null);
			}
		}
		else{
			if(filsDroit != null){
				filsDroit.insert(c, v);
			}
			else{
				filsDroit = new ABR(c, v, null, null);
			}
		}
	}
	public boolean estFeuille(){
		return filsGauche == null && filsDroit == null;
	}
	private int[] estABR_aux(){
		int[] res = {cle, cle, 1};
		if(estFeuille()){
			return res;
		}
		if(filsGauche != null){
			int[] resAux = filsGauche.estABR_aux();
			if(resAux[2] == 0 || resAux[1] > cle){
				res[2] = 0;
			}
			res[0] = Math.min(res[0], resAux[0]);
		}
		if(filsDroit != null){
			int[] resAux = filsDroit.estABR_aux();
			if(resAux[2] == 0 || resAux[0] < cle){
				res[2] = 0;
			}
			res[1] = Math.max(res[1], resAux[1]);
		}
		return res;
	}
	public boolean estABR(){
		return estABR_aux()[2] == 1;
	}
	public static void main(String[] args){
		int[] tab_cles = {1, 2, 3, 4};
		int[] tab_valeurs = {23, 35, 67, 169};
		ABR arbre = new ABR(tab_cles, tab_valeurs);
		System.out.println(arbre.appartient(3));
		System.out.println(arbre.getValeur(3));
		arbre.insert(5, 235235);
		System.out.println(arbre.getValeur(5));
		System.out.println(arbre.estABR());
	}
}
