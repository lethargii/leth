import java.util.ArrayList;

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

	public int nbFeuilles(){
		int res = 0;
		if(filsGauche != null){
			res += filsGauche.nbFeuilles();
		}
		if(filsDroit != null){
			res += filsDroit.nbFeuilles();
		}
		if(filsGauche == null && filsDroit == null){
			res += 1;
		}
		return res;
	}

	public int sommeEtiquettes(){
		int res = valeur;
		if(filsGauche != null){
			res += filsGauche.sommeEtiquettes();
		}
		if(filsDroit != null){
			res += filsDroit.sommeEtiquettes();
		}
		return res;
	}

	public ArrayList<Integer> listeInfixe(){
		ArrayList<Integer> res = new ArrayList<Integer>();
		if(filsGauche != null){
			res = filsGauche.listeInfixe();
		}
		res.add(valeur);
		if(filsDroit != null){
			res.addAll(filsDroit.listeInfixe());
		}
		return res;
	}

	public boolean appartient(int e){
		if(valeur == e){
			return true;
		}
		if(filsGauche != null){
			if(filsGauche.appartient(e)){
				return true;
			}
		}
		if(filsDroit != null){
			if(filsDroit.appartient(e)){
				return true;
			}
		}
		return false;

	}

	public ArrayList<Integer> parents(int e){
		ArrayList<Integer> res = new ArrayList<Integer>();
		if((filsGauche != null && filsGauche.valeur == e) || (filsDroit != null && filsDroit.valeur == e)){
			res.add(valeur);
		}
		if(filsGauche != null){
			res.addAll(filsGauche.parents(e));
		}
		if(filsDroit != null){
			res.addAll(filsDroit.parents(e));
		}
		return res;
	}

	public static int expo2(int n){
		if(n == 1){
			return 2;
		}
		if(n%2 == 0){
			int a = expo2(n/2);
			return a*a;
		}
		int a = expo2((int) n/2);
		return 2 * a * a;
	}

	public int evalue(){
		int res = 0;
		if(filsGauche == null){
			res += 1;
		}
		else{
			res += expo2(filsGauche.evalue());
		}
		if(filsDroit != null){
			res += filsDroit.evalue();
		}
		return res;
	}

	public static int dec2P(int n){
		int p = 0;
		while(expo2(p) > n || expo2(p+1) <= n){
			p += 1;
		}
		return p;
	}

	public static int dec2Q(int n){
		return n - expo2(dec2P(n));
	}

	public static Noeud arbreMini(int n){
		if(n == 0){
			return null;
		}
		return new Noeud(n, arbreMini(dec2P(n)), arbreMini(dec2Q(n)));
	}

	public static Noeud fermat(int n){
		if(n == 0){
			return null;
		}
		return new Noeud(n, arbreMini(expo2(n)), arbreMini(1));
	}

	public static void main(String[] args){
		Noeud n1 = new Noeud(41, null, null);
		Noeud n2 = new Noeud(22, null, null);
		Noeud n3 = new Noeud(15, n1, n2);
		Noeud n4 = new Noeud(41, null, null);
		Noeud n5 = new Noeud(28, n3, n4);
		ArbreBinaire arbreEx = new ArbreBinaire(n5);
		System.out.println(arbreEx.taille());
		System.out.println(arbreEx.hauteur());
		System.out.println(arbreEx.nbFeuilles());
		System.out.println(arbreEx.sommeEtiquettes());
		System.out.println(arbreEx.listeInfixe());
		System.out.println(arbreEx.appartient(41));
		System.out.println(arbreEx.appartient(37));
		System.out.println(arbreEx.parents(41));
		System.out.println(arbreEx.evalue());
		ArbreBinaire juju = new ArbreBinaire(new Noeud(0,null,new Noeud(0,null,null)));
		System.out.println(juju.evalue());
	}
}
