public class Noeud{
	private int valeur;
	private Noeud filsGauche;
	private Noeud filsDroit;

	public Noeud(int valeur, Noeud filsGauche, Noeud filsDroit){
		this.valeur = valeur;
		this.filsGauche = filsGauche;
		this.filsDroit = filsDroit;
	}

	public Noeud getFilsGauche(){
		return filsGauche;
	}

	public Noeud getFilsDroit(){
		return filsDroit;
	}

	public void setFilsGauche(Noeud filsGauche){
		this.filsGauche = filsGauche;
	}

	public void setFilsDroit(Noeud filsDroit){
		this.filsDroit = filsDroit;
	}

	public int taille(){
		int res = 0;
		if(filsGauche != null){
			res += filsGauche.taille();
		}
		if(filsDroit != null){
			res += filsDroit.taille();
		}
		return res + 1;
	}

	public int hauteur(){
		int res = 0;
		if(filsGauche != null){
			res = Math.max(res + 1, filsGauche.hauteur() + 1);
		}
		if(filsDroit != null){
			res = Math.max(res + 1, filsDroit.hauteur() + 1);
		}
		return res;
	}

	public static void main(String[] args){
		Noeud n1 = new Noeud(22, null, null);
		Noeud n2 = new Noeud(41, null, null);
		Noeud n3 = new Noeud(15, n1, n2);
		Noeud n4 = new Noeud(41, null, null);
		Noeud n5 = new Noeud(28, n3, n4);
		ArbreBinaire a1 = new ArbreBinaire(n5);
		System.out.println(a1.taille());
		System.out.println(a1.hauteur());
		System.out.println();
	}
}
