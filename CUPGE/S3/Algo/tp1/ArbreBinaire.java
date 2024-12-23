import java.util.ArrayList;

public class ArbreBinaire{
	private Noeud racine;

	public ArbreBinaire(Noeud racine){
		this.racine = racine;
	}

	public int taille(){
		if(racine == null){
			return 0;
		}
		return racine.taille();
	}

	public int hauteur(){
		if(racine == null){
			return -1;
		}
		return racine.hauteur();
	}
	
	public int nbFeuilles(){
		if(racine == null){
			return 0;
		}
		return racine.nbFeuilles();
	}

	public int sommeEtiquettes(){
		if(racine == null){
			return 0;
		}
		return racine.sommeEtiquettes();	
	}

	public ArrayList<Integer> listeInfixe(){
		if(racine == null){
			return new ArrayList<Integer>();
		}
		return racine.listeInfixe();
	}

	public boolean appartient(int e){
		if(racine == null){
			return false;
		}
		return racine.appartient(e);
	}

	public ArrayList<Integer> parents(int e){
		if(racine == null){
			return new ArrayList<Integer>();
		}
		return racine.parents(e);
	}

	public int evalue(){
		if(racine == null){
			return 0;
		}
		return racine.evalue();
	}

	public static ArbreBinaire arbreMini(int n){
		return new ArbreBinaire(Noeud.arbreMini(n));
	}

	public static ArbreBinaire fermat(int n){
		return new ArbreBinaire(Noeud.fermat(n));
	}
}
