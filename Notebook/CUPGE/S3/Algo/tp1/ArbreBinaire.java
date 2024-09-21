public class ArbreBinaire{
	private Noeud racine;

	public ArbreBinaire(Noeud racine){
		this.racine = racine;
	}

	public int taille(){
		return racine.taille();
	}

	public int hauteur(){
		return racine.hauteur();
	}
}
