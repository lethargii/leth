public class Magasin{
	Produit[] produits;
	int nbProduits;
	public Magasin(){
		produits = new Produit[1000];
		nbProduits = 0;
	}
	public void ajouteProduit (Produit p){
		produits[nbProduits] = p;
		nbProduits +=	1;
	}
	public Produit choisitProduit(String nomProduit){
		Produit produitChoisi = null;
		for(int i = 0; i < nbProduits; i++){
			if(produits[i].getNom() == nomProduit){
				produitChoisi = produits[i];
				nbProduits--;
				for(int j = i; j < nbProduits; j++){
					produits[j] = produits[j+1];
				}
				return produitChoisi;
			}
		}
		return produitChoisi;
	}
	public String toString(){
		String res = "Magasin, produits :\n";
		for(int i = 0; i < nbProduits; i++){
			res += "	" + produits[i] + "\n";
		}
		return res;
	}
}
