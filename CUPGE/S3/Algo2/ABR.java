import java.util.ArrayList;

public class ABR{
	ABR filsGauche;
	ABR filsDroit;
	int valeur;
	public ABR(ABR filsGauche, ABR filsDroit, int valeur){
		this.filsGauche = filsGauche;
		this.filsDroit = filsDroit;
		this.valeur = valeur;
	}
	public ABR(int[] tab){
		if(tab.length < 3){
			if(tab.length == 2){
				valeur = tab[0];
				filsDroit = new ABR(null, null, tab[1]);
			}
			else{
				valeur = tab[0];
			}
		}
		else{
			int m = tab.length/2;
			this.valeur = tab[m];
			int[] tabFG = new int[m-1];
			for(int i = 0; i < m ; i++){
				tabFG[i] = tab[i];
			}
			int[] tabFD = new int[tab.length-m-1];
			for(int i = m+1; i < tab.length ; i++){
				tabFD[i] = tab[i];
			}
			this.filsGauche = new ABR(tabFG);
			this.filsDroit = new ABR(tabFD);
		}
	}
	public boolean estABR(){
		return false;
	}
	public ArrayList<Integer> parcours(){
		ArrayList<Integer> res = new ArrayList<Integer>();
		return res;
	}
	public boolean recherche(int blabla){
		if(blabla < this.valeur && filsGauche != null){
			return filsGauche.recherche(blabla);
		}
		if(blabla > this.valeur && filsDroit != null){
			return filsDroit.recherche(blabla);
		}
		if(blabla == this.valeur){
			return true;
		}
		return false;
	}
	public void insert(int nval){
		// Cas ou on doit inserer la valeur à gauche et où le fils gauche existe déjà
		if(nval < this.valeur && filsGauche == null){
			filsGauche = new ABR(null, null, valeur);
		}
		if(nval < this.valeur && filsGauche != null){
			filsGauche.insert(nval);
		}
		if(nval > this.valeur && filsDroit == null){
			filsDroit = new ABR(null, null, valeur);
		}
		if(nval > this.valeur && filsDroit != null){
			filsDroit.insert(nval);
		}
	}
	public int taille(){
		int compteur = 1;
		if(filsGauche != null){
			compteur += filsGauche.taille();
		}
		if(filsDroit != null){
			compteur += filsDroit.taille();
		}
		return compteur;
	}
	public int hauteur(){
		int hauteurFG = 0;
		int hauteurFD = 0;
		if(filsGauche != null){
			hauteurFG = filsGauche.hauteur();
		}
		if(filsDroit != null){
			hauteurFD = filsDroit.hauteur();
		}
		return Math.max(hauteurFG, hauteurFD) + 1;
	}
}
